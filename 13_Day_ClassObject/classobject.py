# Class dengan default Attribute

class Car:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def keterangan(self):
        print(f"Mobil baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer}")

mobil_baru = Car('Honda','City',2021)
mobil_baru.keterangan()

# Multiple Object

class Kucing():
    def __init__(self, ras, umur):
        self.ras = ras
        self.umur = umur

    def tampil(self):
        print(f"Kucingku berjenis {self.ras} dengan umur {self.umur} bulan")

kucing_saya = Kucing("persia",2)
kucing_dia = Kucing("anggora",3)

kucing_saya.tampil()
kucing_dia.tampil()

# Attribute Class yang merupakan Instance dari Class lain

class Kucing():
    def __init__(self, ras, umur):
        self.ras = ras
        self.umur = umur

class Pemilik():
    def __init__(self,nama,alamat, kucing):
        self.nama = nama
        self.alamat = alamat
        self.kucing = kucing

    def tampil(self):
        print(f"Halo, aku {self.nama} berasal dari {self.alamat}")
        print(f"Kucingku berjenis {self.kucing.ras} dengan umur {self.kucing.umur} bulan")


arif = Pemilik(
    nama = "Arif",
    alamat = "Solo",
    kucing = Kucing(
        ras = "Persia",
        umur = 7
    )
)

arif.tampil()