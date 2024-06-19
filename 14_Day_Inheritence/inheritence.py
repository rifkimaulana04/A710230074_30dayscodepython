# Atribut dan Method baru untuk Class Turunan

class Car:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def keterangan(self):
        print(f"Mobil baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer}")


class ElectricCar(Car):
    def __init__(self, merk, model, tahun, baterai):
        super().__init__(merk, model, tahun)
        self.baterai = baterai

    def daya(self):
        print(f"Mobil ini memiliki daya {self.baterai} -kWh")

teslaku = ElectricCar('tesla', 'model X', 2022, 7500)
print(teslaku.daya())

# Override (Menimpa) method Class Induk

class Car:
    def __init__(self, merk, model, tahun, odometer):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = odometer

    def keterangan(self):
        print(f"Mobil baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer}")

    def gantioli(self):
        print(f"Mobil {self.merk} ini perlu ganti oli ketika odometer {self.odometer}")


class ElectricCar(Car):
    def __init__(self, merk, model, tahun, odometer, baterai):
        super().__init__(merk, model, tahun, odometer)
        self.baterai = baterai  
        
    def daya(self):
        print(f"Mobil ini memiliki daya {self.baterai} -kWh")   
    
    def gantioli(self):
        print(f"Mobil listrik tidak memerlukan ganti oli")


alphardku = Car('toyota', 'alphard', 2022, 10000)
print(alphardku.gantioli())

teslaku = ElectricCar('tesla', 'model X', 2022, 10000, 7500)
print(teslaku.gantioli())

# Multiple Class Inheritence 

class Penjumlahan:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def jumlah(self):
        return self.angka1 + self.angka2

class Perkalian():
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def kali(self):
        return self.angka1 * self.angka2


class Pembagian(Penjumlahan, Perkalian):

    def bagi(self):
        return self.angka1 / self.angka2


hitung = Pembagian(8, 2)
print(hitung.kali())
print(hitung.bagi())
print(hitung.jumlah())