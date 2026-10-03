# Input: Meminta nilai ujian rentang 0 sampai 100 bertipe float
# Proses: Memeriksa apakah nilai berada di luar rentang (kurang dari 0 atau lebih dari 100)
# Kondisi Berhenti: Loop akan berhenti ketika user memasukkan input nilai di rentang 0-100 (kondisi while menjadi False)
# Output: Menampilkan "Nilai tidak valid" saat salah, dan "Nilai diterima" ketika input sesuai

nilai = float(input("Nilai 0-100: "))

# Selama nilai kurang dari 0 atau lebih dari 100, program akan terus meminta input
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")