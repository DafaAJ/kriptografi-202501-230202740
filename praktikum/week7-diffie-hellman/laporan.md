# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-Hellman Key Exchange  
Nama: Dafa Afriza Julianto  
NIM: 230202740  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Melakukan simulasi protokol **Diffie-Hellman** untuk pertukaran kunci publik.  
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.  
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan **Man-in-the-Middle / MITM**).

---

## 2. Dasar Teori
Diffie-Hellman adalah protokol kriptografi yang memungkinkan dua pihak (mis. Alice dan Bob) menghasilkan kunci bersama (shared secret) melalui saluran publik. Keamanan dasar Diffie-Hellman bergantung pada kesulitan menyelesaikan masalah logaritma diskrit: jika 𝑝 adalah bilangan prima dan 𝑔 generator modulo 𝑝, maka dari publik 𝑔<sup>𝑎</sup> mod 𝑝 sulit untuk menemukan 𝑎 tanpa informasi tambahan.

Protokol berjalan dengan memilih parameter publik 𝑝 (prima) dan 𝑔 (generator), lalu masing-masing pihak memilih private key 𝑎 dan 𝑏. Mereka menghitung public key 𝐴 = 𝑔<sup>𝑎</sup> mod 𝑝 dan 𝐵 = 𝑔<sup>𝑏</sup> mod 𝑝 dan saling bertukar. Kunci bersama dihitung sebagai 𝐾 = 𝐵<sup>𝑎</sup> mod 𝑝=𝐴<sup>𝑏</sup> mod 𝑝=𝑔<sup>𝑎𝑏</sup> mod 𝑝. Kelemahan utama tanpa autentikasi adalah rentan terhadap serangan Man-in-the-Middle (MITM): penyerang yang mengontrol saluran dapat mengganti public key sehingga pihak yang berkomunikasi berakhir dengan kunci yang berbeda dan penyerang tahu kunci kedua pihak.

---

## 3. Alat dan Bahan
(- Python 3.12.10  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `diffie_hellman.py` di folder `praktikum/week7-diffie-hellman/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python diffie_hellman.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)
)

---

## 7. Jawaban Pertanyaan  
- Pertanyaan 1: Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?  
  Karena keamanan bergantung pada masalah logaritma diskrit: walau publik nilai 𝑔<sup>𝑎</sup> mod 𝑝 dan 𝑔<sup>𝑏</sup> mod 𝑝 terlihat di jaringan, tanpa mengetahui 𝑎 atau 𝑏 sangat sulit (untuk p besar) menghitung 𝑔<sup>𝑎𝑏</sup>. Oleh karena itu dua pihak bisa membuat kunci bersama meski komunikasi bersifat publik.
- Pertanyaan 2: Apa kelemahan utama protokol Diffie-Hellman murni?  
  Kelemahan utama adalah ketiadaan autentikasi: protokol rentan terhadap serangan MITM yang dapat mengganti public key pada saat pertukaran sehingga penyerang dapat memediasi dan mengetahui atau memanipulasi kunci.
- Pertanyaan 3: Bagaimana cara mencegah serangan MITM pada protokol ini?  
  * Terapkan autentikasi (digital signature, certificate/PKI).
  * Gunakan protokol aman seperti TLS yang menggabungkan DH dengan sertifikat.
  * Verifikasi fingerprint kunci secara out-of-band apabila memungkinkan.
  * Gunakan authenticated Diffie-Hellman variants (mis. Station-to-Station protocol).

---

## 8. Kesimpulan
Dari hasil percobaan, dapat disimpulkan bahwa algoritma Diffie-Hellman Key Exchange memungkinkan dua pihak untuk menghasilkan kunci rahasia bersama meskipun komunikasi dilakukan melalui saluran publik. Proses pertukaran ini terbukti berhasil ketika kedua pihak menggunakan parameter publik yang sama tanpa adanya gangguan. Namun, percobaan simulasi serangan menunjukkan bahwa protokol Diffie-Hellman murni memiliki kelemahan serius jika tidak disertai mekanisme autentikasi, karena pihak ketiga (Eve) dapat melakukan serangan Man-in-the-Middle dan mengetahui kunci rahasia kedua pihak. Oleh karena itu, penerapan Diffie-Hellman di dunia nyata harus disertai autentikasi seperti tanda tangan digital atau sertifikat untuk mencegah penyusupan dan menjaga kerahasiaan komunikasi.

---

## 9. Daftar Pustaka
-

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
