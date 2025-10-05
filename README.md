Active Proxy Scraper & Checker, sebuah tool Python yang cepat dan andal. Tujuannya adalah untuk mengumpulkan daftar proxy HTTP/S yang besar dari berbagai sumber dan memvalidasi keaktifannya menggunakan threading berkecepatan tinggi. Hanya proxy yang aktif dan berfungsi yang akan disimpan ke file output (proxies.txt).

Deskripsi
Pengambilan Proxy Otomatis	Mengambil proxy mentah dari tujuh endpoint GitHub/API yang stabil.
Validasi Kecepatan Tinggi	Menggunakan threading (50 worker secara default) untuk memvalidasi proxy secara simultan.
Hanya Proxy Aktif	Hanya proxy yang berhasil terhubung ke target (Google.com) dalam batas waktu yang ditentukan yang disimpan.
Antarmuka Interaktif	Menggunakan colorama untuk output berwarna dan tqdm untuk bilah kemajuan (progress bar) visual yang threading-safe.
Instalasi Otomatis	Menginstal semua library Python (requests, colorama, tqdm) secara otomatis dengan opsi paksa (--break-system-packages).

# 🔥 Active Proxy Scraper & Checker (Fast Threaded)

Alat Python yang cepat dan andal untuk mengumpulkan daftar besar proxy HTTP/S dari berbagai sumber daring dan memvalidasi keaktifannya menggunakan *threading*. Hanya proxy yang aktif dan berfungsi yang akan disimpan ke file output.

## 🌟 Fitur Utama

* **Pengambilan Proxy Otomatis:** Mengambil daftar proxy mentah dari tujuh *endpoint* GitHub/API yang stabil.
* **Validasi Kecepatan Tinggi:** Menggunakan *threading* (50 *worker* secara *default*) untuk memvalidasi proxy secara simultan, sehingga proses *checking* menjadi sangat cepat.
* **Hanya Proxy Aktif:** Hanya proxy yang berhasil terhubung ke target (Google.com) dalam batas waktu yang ditentukan yang akan disimpan.
* **Antarmuka Pengguna Interaktif:** Menggunakan **`colorama`** untuk *output* berwarna dan **`tqdm`** untuk bilah kemajuan (*progress bar*) visual yang *threading-safe*.
* **Instalasi Otomatis:** Secara otomatis menginstal semua *library* Python yang diperlukan (`requests`, `colorama`, `tqdm`) dengan opsi paksa (`--break-system-packages`).

---

## 🛠️ Instalasi dan Penggunaan

### 1. Prasyarat

Anda hanya membutuhkan **Python 3** dan **`pip`** yang terinstal di sistem Anda.

### 2. File Skrip

Pastikan Anda memiliki file skrip **`color_proxy_checker.py`** di direktori yang sama.

### 3. Eksekusi (Disarankan)

Karena skrip akan secara otomatis menginstal dependensi Python dan karena menjalankan *proxy checker* seringkali membutuhkan izin jaringan yang lebih tinggi di beberapa lingkungan Linux, disarankan untuk menjalankan skrip menggunakan `sudo`.

```bash
# Perintah untuk menjalankan tool:
sudo python3 color_proxy_checker.py
