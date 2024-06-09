# Menerima input dari pengguna
nama_depan = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")
nim = input("Masukkan NIM: ")

# Menggabungkan nama depan dan nama belakang menjadi satu variabel
nama_lengkap = nama_depan + " " + nama_belakang

# Menghitung lebar layar (dalam jumlah karakter)
lebar_layar = 50

# Mencetak output sesuai format yang diminta
print()
print("Pendidikan Teknik Informatika".center(lebar_layar))
print("Nama : " + nama_lengkap)
print("Nim : " + nim)
print("Fakultas Keguruan dan Ilmu Pendidikan")
print("UNIVERSITAS MUHAMMADIYAH SURAKARTA".upper().center(lebar_layar))