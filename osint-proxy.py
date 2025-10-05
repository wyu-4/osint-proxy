import os
import subprocess
import sys
import re
import time
import requests
from threading import Thread, Lock
from queue import Queue
from tqdm import tqdm # Import TQDM untuk Progress Bar
from colorama import Fore, Style, init # Import Colorama untuk Warna

# Inisialisasi Colorama untuk memastikan warna bekerja di semua terminal
init(autoreset=True) 

# --- Konfigurasi ---
OUTPUT_FILENAME = "proxies.txt"
# Daftar endpoint proxy HTTP/S yang diperluas
PROXY_ENDPOINTS = [
    "https://api.proxyscrape.com/v3/free-proxy-list/get/http?request=displaymode&protocol=http",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/proxy-nl/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/official-dev/proxy-list/main/http.txt",
]
REQUIRED_PACKAGES = ['requests', 'colorama', 'tqdm'] # TAMBAHAN
CHECK_TIMEOUT = 5  # Waktu tunggu (detik) per proxy saat validasi
MAX_WORKERS = 50   # Jumlah thread untuk validasi
# --- End Konfigurasi ---

# Variabel Global untuk Validasi
active_proxies = []
print_lock = Lock()
pbar = None # Variabel global untuk progress bar

def install_packages():
    """Memeriksa dan menginstal pustaka Python yang hilang menggunakan --break-system-packages."""
    print(Fore.YELLOW + "----------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.CYAN + "[*] Checking for required Python packages...")
    packages_to_install = []
    
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            packages_to_install.append(package)

    if not packages_to_install:
        print(Fore.GREEN + "[+] All Python packages found. Proceeding." + Style.RESET_ALL)
        return True

    print(Fore.RED + f"[-] Missing packages: {', '.join(packages_to_install)}. Attempting automatic installation (FORCED)..." + Style.RESET_ALL)
    
    pip_command = [sys.executable, "-m", "pip", "install"] + packages_to_install + ["--break-system-packages"]

    try:
        subprocess.check_call(pip_command)
        print(Fore.GREEN + "[+] Python packages installed successfully." + Style.RESET_ALL)
        return True
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] ERROR: Failed to install packages. Detail: {e}" + Style.RESET_ALL)
        return False

# Panggil fungsi instalasi
if not install_packages():
    sys.exit(1)


def get_proxies_direct(endpoints):
    """Mengambil proxy dari daftar endpoint langsung."""
    print(Fore.YELLOW + "----------------------------------------------------------" + Style.RESET_ALL)
    unique_proxies = set()
    proxy_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}'

    for url in endpoints:
        print(Fore.CYAN + f"[*] Fetching data from: {url}...")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status() 
            proxies = re.findall(proxy_pattern, response.text)
            
            if proxies:
                unique_proxies.update(proxies)
                
        except requests.exceptions.RequestException:
            pass 
        
    final_list = list(unique_proxies)
    print(Fore.GREEN + f"[+] Total {len(final_list)} unique raw proxies collected." + Style.RESET_ALL)
    return final_list

# --- FUNGSI PROXY CHECKING ---

def check_proxy(q):
    """Fungsi yang akan dijalankan oleh setiap thread untuk memvalidasi proxy."""
    global pbar
    while True:
        proxy = q.get()
        if proxy is None:
            break
            
        try:
            proxies_dict = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
            # Coba terhubung ke situs yang stabil
            requests.get("http://www.google.com", proxies=proxies_dict, timeout=CHECK_TIMEOUT)
            
            # Jika berhasil, tambahkan ke daftar aktif
            with print_lock:
                active_proxies.append(proxy)
                # TQDM otomatis mengurus output, tidak perlu print biasa
                pbar.set_description(f"{Fore.GREEN}Active: {len(active_proxies)}{Style.RESET_ALL}")

        except requests.exceptions.RequestException:
            pass
        except Exception:
            pass
            
        # Update progress bar
        with print_lock:
            pbar.update(1)
            
        q.task_done()

def run_checker(proxy_list):
    """Mengelola threading dan progress bar untuk validasi proxy."""
    global pbar
    print(Fore.YELLOW + "----------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"[*] Starting proxy validation with {MAX_WORKERS} workers. Timeout: {CHECK_TIMEOUT}s..." + Style.RESET_ALL)

    queue = Queue()
    threads = []
    
    # Membuat dan memulai thread worker
    for _ in range(MAX_WORKERS):
        t = Thread(target=check_proxy, args=(queue,))
        t.start()
        threads.append(t)

    # Inisialisasi Progress Bar (Grafik)
    pbar = tqdm(total=len(proxy_list), desc="Checking Proxies", unit=" proxy", dynamic_ncols=True, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}] {desc}")

    # Memuat semua proxy ke dalam antrian
    for proxy in proxy_list:
        queue.put(proxy)

    # Tunggu sampai semua item di antrian diproses
    queue.join()

    # Beri sinyal thread untuk berhenti
    for _ in range(MAX_WORKERS):
        queue.put(None)
    for t in threads:
        t.join()

    # Tutup progress bar
    pbar.close()

    print(Fore.YELLOW + f"----------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + f"[+] CHECK COMPLETE: Found {len(active_proxies)} active proxies." + Style.RESET_ALL)
    return active_proxies


def save_to_file(proxies, filename):
    """Menyimpan daftar proxy aktif ke file teks."""
    if not proxies:
        return
        
    try:
        with open(filename, 'w') as f:
            for proxy in proxies:
                f.write(proxy + '\n')
        
        print(Fore.GREEN + f"[+] Successfully saved {len(proxies)} active proxies to: {os.path.abspath(filename)}" + Style.RESET_ALL)
    except IOError as e:
        print(Fore.RED + f"[-] Error writing to file: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    # 1. Ambil semua proxy mentah
    raw_proxies = get_proxies_direct(PROXY_ENDPOINTS)
    
    if raw_proxies:
        # 2. Validasi proxy menggunakan threading dan progress bar
        valid_proxies = run_checker(raw_proxies)
        
        # 3. Simpan hanya proxy yang aktif
        save_to_file(valid_proxies, OUTPUT_FILENAME)
    else:
        print(Fore.RED + "[-] Cannot proceed to check. No raw proxies were collected." + Style.RESET_ALL)