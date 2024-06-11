# Program untuk menentukan diskon tarif kereta api berdasarkan umur penumpang

# Mendapatkan input dari pengguna
tahun_lahir = int(input("Masukkan tahun kelahiran penumpang: "))
harga_tiket = float(input("Masukkan harga tiket kereta api: "))

# Menghitung umur penumpang
tahun_sekarang = 2024  # Misalkan tahun sekarang adalah 2024
umur = tahun_sekarang - tahun_lahir

# Menentukan diskon berdasarkan umur
if 0 <= umur <= 4:
    diskon = 1.0  # 100% diskon
elif 5 <= umur <= 12:
    diskon = 0.5  # 50% diskon
else:
    diskon = 0.0  # Tidak ada diskon

# Menghitung harga akhir setelah diskon
harga_akhir = harga_tiket * (1 - diskon)

# Menampilkan hasil
print(f"Umur penumpang: {umur} tahun")
print(f"Diskon: {diskon * 100}%")
print(f"Harga tiket setelah diskon: Rp {harga_akhir:.2f}")