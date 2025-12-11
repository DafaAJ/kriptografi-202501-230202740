# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: Public Key Infrastructure (PKI & Certificate Authority)  
Nama: Dafa Afriza Julianto  
NIM: 230202740  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.  
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.  
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS). 

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah sistem yang digunakan untuk mengelola pasangan kunci publik–privat serta menerbitkan sertifikat digital. Sertifikat digital mengikat identitas (nama domain, organisasi, negara) dengan sebuah public key, dan biasanya diterbitkan oleh Certificate Authority (CA). PKI memastikan bahwa entitas yang terhubung dalam komunikasi memiliki identitas yang sah dan dapat dipercaya.

Certificate Authority (CA) adalah lembaga terpercaya yang bertugas menerbitkan dan memverifikasi sertifikat digital. CA menandatangani sertifikat menggunakan private key mereka sehingga browser atau sistem lain dapat memverifikasi sertifikat tersebut menggunakan public key CA. Dengan cara ini, PKI mendukung keaslian, integritas, dan non-repudiation dalam komunikasi aman.

Sertifikat digital banyak digunakan dalam HTTPS/TLS. Ketika pengguna mengakses situs web, browser memeriksa apakah sertifikat situs tersebut valid, tidak kedaluwarsa, tidak dicabut, dan ditandatangani oleh CA yang terpercaya. Tanpa PKI, komunikasi online rawan terhadap serangan seperti man-in-the-middle (MITM) atau spoofing.

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
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

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
