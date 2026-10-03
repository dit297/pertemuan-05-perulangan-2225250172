# Input: Program menerima satu bilangan bulat n
# Proses: Melakukan iterasi dari 1 sampai 10 dan mengalikannya dengan n
# Kondisi Berhenti: Iterasi berhenti ketika mencapai batas akhir range (yaitu 10)
# Output: Menampilkan string perkalian "n x i = hasil"

n = int(input("Bilangan: "))

# Range 1 sampai 11, karena nilai batas akhir 11 tidak ikut dipakai sehingga akan berhenti di 10
for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")