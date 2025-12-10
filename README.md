🔍 IP Tracker Console – Python

Skrip Python sederhana untuk melakukan IP Lookup menggunakan API ifconfig.co.
Fitur dapat menampilkan informasi IP target atau IP perangkat sendiri,lengkap dengan negara, kota, ISP, dan zona waktu.

---

✨ Fitur Utama

· 🔐 Login password sebelum masuk menu
· 🌍 Lihat Informasi IP Target
· 🖥️ Lihat IP Perangkat Sendiri
· ⏳ Animasi delay biar tampilan lebih keren
· 🎨 Warna teks (Colorama)

---

🛠 Persyaratan

Sebelum menjalankan skrip, pastikan kamu sudah install:

· Python 3
· pip (biasanya sudah ada di Python)

---

📦 Cara Install

Termux / Linux / Windows

1. Jalankan perintah untuk install dependencies:
   ```bash
   pip install requests colorama
   ```
2. Clone repository:
   ```bash
   git clone https://github.com/agusjawirtechid/Python-oisint-ip
   cd Python-oisint-ip
   ```
3. Jalankan skrip:
   ```bash
   python cekip.py
   ```

---

🔐 Login

Saat program berjalan akan muncul:

```
masukan password:
```

Masukkan password:

```
agusganteng
```

Jika benar, kamu akan masuk ke menu:

```
1. lihat ip orang lain
2. lihat ip sendiri
pilih 1/2 :
```

---

📘 Cara Menggunakan

1️⃣ Lihat IP Orang Lain

Pilih:

```
1
```

Masukkan IP target, contoh:

```
MASUKAN IP TARGET: 8.8.8.8
```

Tampilan output akan muncul seperti:

```
==========================
 HASIL DATA IP TARGET
==========================

IP: 8.8.8.8
negara: United States
wilayah: California
kota: Mountain View
zona waktu: America/Los_Angeles
penyedia jaringan: Google LLC
```

2️⃣ Lihat IP Sendiri

Pilih:

```
2
```

Output akan menampilkan detail IP perangkat kamu:

```
==========================
HASIL DATA PERANGKAT
==========================

IP: x.x.x.x
negara: Indonesia
wilayah: Bali
kota: Denpasar
zona waktu: Asia/Makassar
penyedia jaringan: Telkom Indonesia
```

---

📁 File Program

Kode program utama ada di file iptracker.py dalam repository ini.

---

💡 Catatan

· API menggunakan layanan gratis ifconfig.co
· Informasi lokasi IP tidak selalu 100% akurat
· Gunakan script ini untuk keperluan edukasi dan pembelajaran

---

⭐ Support

Jika kamu suka project ini, jangan lupa kasih star ⭐ di GitHub!

https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github

---

📄 Lisensi

Project ini dibuat untuk tujuan edukasi. Penggunaan harus sesuai dengan hukum yang berlaku di wilayah Anda.

Dibuat dengan ❤️ oleh Agus
