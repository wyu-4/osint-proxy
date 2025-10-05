Deskripsi
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
```
### 4. Setelah proses scraping dan validasi selesai, hasilnya akan disimpan di:

proxies.txt: File teks yang hanya berisi daftar proxy yang ditemukan aktif, dengan format IP:PORT (satu proxy per baris).

⚠️ Peringatan Penting (Disclaimer)
Gunakan Alat Ini Dengan Risiko Anda Sendiri!

Izin sudo: Skrip memerlukan sudo untuk memastikan instalasi dependensi Python berhasil di lingkungan Linux. Selalu berhati-hati saat menjalankan skrip Python dengan hak akses root.

Legalitas Proxy: Proxy yang dikumpulkan dari sumber terbuka daring seringkali ilegal atau tidak etis untuk digunakan dalam aktivitas yang memerlukan izin atau anonimitas penuh. Penulis skrip ini tidak bertanggung jawab atas penggunaan proxy hasil tool ini untuk tujuan ilegal, berbahaya, atau yang melanggar ketentuan layanan situs web mana pun.

Kualitas Proxy: Proxy gratis bersifat sementara. Proxy yang aktif saat divalidasi mungkin mati dalam hitungan jam, menit, atau bahkan detik. Disarankan untuk menggunakan proxy yang baru divalidasi secepat mungkin.
