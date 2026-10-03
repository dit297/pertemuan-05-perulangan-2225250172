# Input: Suku pertama (a), beda (d) sebagai float, dan banyak suku (n) sebagai int.
# Proses: Menghitung nilai suku ke-i dengan rumus a + (i * d) dan mengakumulasi nilainya.
# Kondisi Berhenti: Pada loop while, berhenti saat n positif. Pada loop for, berhenti setelah mengulang n kali.
# Output: Menampilkan nomor suku beserta nilainya, serta total jumlah deret (2 angka di belakang koma).

print("Deret Aritmetika")

# 1. Baca a dan d
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

# 2. Baca n dan lakukan validasi berulang jika n <= 0
n = int(input("Banyak suku n: "))

while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

# 3. Set total = 0 di luar perulangan
total = 0

# 4. Ulangi i dari 0 sampai n-1
for i in range(n):
    # 5. Hitung suku
    suku = a + (i * d)
    
    # 6. Tambahkan suku ke total dan tampilkan suku
    total += suku
    # +1 digunakan pada {i+1} agar tampilan nomor suku dimulai dari 1, bukan 0
    print(f"Suku ke-{i+1}: {suku:.2f}")

# 7. Setelah loop selesai, tampilkan total dengan 2 angka di belakang koma
print(f"Jumlah: {total:.2f}")