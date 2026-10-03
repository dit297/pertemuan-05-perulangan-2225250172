# Pertemuan 05 Perulangan Python

**Nama:** Aditya Setianugroho
**NIM:** 2225250172
**Kelas:** 3F

## Tujuan
Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif, menelusuri perubahan variabel, menguji kondisi berhenti, dan menggabungkan seleksi dengan perulangan untuk menyelesaikan masalah matematis.

## Cara Menjalankan
Pastikan terminal berada di root folder proyek (`pertemuan-05-perulangan-2225250172/`), lalu jalankan perintah berikut untuk menguji kuis:
```bash
python kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2
Berikut adalah langkah-langkah perulangan untuk menyelesaikan Kuis 2 Deret Aritmetika:

1.Meminta input untuk suku pertama (a) dan beda (d) dalam tipe data float.

2.Meminta input untuk banyak suku (n) dalam tipe integer.

3.Melakukan validasi input menggunakan while: Jika nilai n <= 0, program akan menolak dan terus meminta input n yang baru sampai user memasukkan bilangan bulat positif.

4.Menyiapkan variabel akumulator total = 0 sebelum perulangan dimulai untuk menyimpan jumlah keseluruhan suku.

5.Memulai perulangan for i in range(n) yang akan beriterasi sebanyak n kali.

6.Di dalam perulangan, program akan menghitung nilai suku saat ini menggunakan rumus suku = a + (i * d).

7.Menambahkan nilai suku tersebut ke dalam variabel total.

8.Menampilkan nilai suku pada setiap iterasi dengan format dua angka di belakang koma.

9.Setelah perulangan selesai, program menampilkan total dari deret tersebut dengan format dua angka di belakang koma.

## Hasil Pengujian
Berikut adalah pencatatan input dan output aktual dari test case wajib Kuis 2:

| Uji | a | d | n | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|-----|---|---|---|--------------------------|-----------------|--------|
| 1 | 2 | 3 | 5 | Suku: 2, 5, 8, 11, 14. Jumlah: 40 | Suku: 2, 5, 8, 11, 14. Jumlah: 40.00 | Sukses |
| 2 | 10 | -2 | 4 | Suku: 10, 8, 6, 4. Jumlah: 28 | Suku: 10, 8, 6, 4. Jumlah: 28.00 | Sukses |
| 3 | 1.5 | 0.5 | 3 | Suku: 1.5, 2.0, 2.5. Jumlah: 6.0 | Suku: 1.5, 2.0, 2.5. Jumlah: 6.00 | Sukses |

## Refleksi
Kesalahan yang Ditemukan: Awalnya, akumulator total = 0 diletakkan di dalam badan perulangan for. Hal ini menyebabkan nilai total selalu direset menjadi 0 pada setiap iterasi, sehingga hasil akhir penjumlahan menjadi tidak akurat (hanya menampilkan nilai suku terakhir).
Cara Memperbaikinya: Variabel total = 0 harus diinisialisasi sebelum perulangan (di luar blok for), sehingga nilainya dapat diakumulasikan secara bertahap setiap kali iterasi berjalan tanpa mengalami reset.