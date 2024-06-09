# Bekerja dengan tipe data Integer

# fungsi imput() akan membaca inputan menjadi string
umur = input('Masukkan umur kamu sekarang : ')
print(type(umur))

#ubah string ke int untuk melakukan operasi aritmatika
umur_baru = int(umur) + 10
print('Umur kamu 10 tahun lagi adalah : ', umur_baru)

# Bekerja dengan tipe data Float

angka_1 = input('Masukkan angka 1 :')
angka_2 = input('Masukkan angka 2 :')
hasil_bagi = float(angka_1) / float(angka_2)
hasil_modulus = float(angka_1) % float(angka_2)
print('Hasil angka 1 dibagi angka 2 = ', hasil_bagi)
print('Hasil modulus angka 1 dengan angka 2 = ', hasil_modulus)

# Bekerja dengan tipe data String

#deklarasi string
jml_mangga = "34"
jml_semangka = "15"
#penjumlahan jika tipe data string
total_buah = jml_mangga + jml_semangka
print(total_buah)
#penjumlahan jika tipe data diubah ke int
total_buah = int(jml_mangga) + int(jml_semangka)
print(total_buah)
      
# Program untuk mengkonversi jarak dari kilometer ke meter

# Meminta input dari pengguna berupa jarak dalam kilometer
kilometer = input("Masukkan jarak dalam kilometer: ")

# Mengubah input dari pengguna menjadi tipe integer
kilometer = int(kilometer)

# Melakukan perhitungan untuk mencari jarak dalam meter
meter = kilometer * 1000

# Menampilkan output berupa jarak dalam meter
print(f"Jarak dalam meter: {meter} meter")