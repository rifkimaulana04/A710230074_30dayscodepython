# Program untuk menentukan apakah sebuah angka positif, negatif, atau nol

# Meminta input dari pengguna
angka = float(input("Masukkan sebuah angka: "))

# Percabangan if-elif-else
if angka > 0:
    print("Angka tersebut adalah positif.")
elif angka < 0:
    print("Angka tersebut adalah negatif.")
else:
    print("Angka tersebut adalah nol.")