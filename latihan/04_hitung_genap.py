# Input: Program menerima bilangan bulat positif n
# Proses: Melakukan iterasi dari 1 sampai n, dan menggunakan logika modulo untuk memeriksa apakah bilangan itu genap. Jika iya, variabel jumlah_genap bertambah 1.
# Kondisi Berhenti: Loop selesai setelah mengecek semua angka hingga n.
# Output: Menampilkan banyaknya bilangan genap yang ditemukan.

n = int(input("n: "))

# Counter dimulai dari 0
jumlah_genap = 0

for i in range(1, n + 1):
    # Seleksi bersarang di dalam perulangan untuk memeriksa sisa bagi
    if i % 2 == 0:
        jumlah_genap += 1

print(f"Banyak bilangan genap: {jumlah_genap}")