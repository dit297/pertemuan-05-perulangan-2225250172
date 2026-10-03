# Input: Program menerima bilangan bulat positif n
# Proses: Mengakumulasi penjumlahan (total + i) dari 1 sampai n
# Kondisi Berhenti: Iterasi berhenti setelah memproses nilai i = n (batas range n+1)
# Output: Menampilkan hasil akhir jumlah total bilangan

n = int(input("n: "))

# Variabel total dimulai dari 0 dan ditempatkan sebelum loop
total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah {total}")