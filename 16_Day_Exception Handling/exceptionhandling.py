# Exception Handler pada Python

try:
    # blok kode yang mungkin menimbulkan exception
    num1 = int(input("Masukkan angka pertama: "))
    num2 = int(input("Masukkan angka kedua: "))
    hasil = num1 / num2
    print(f"Hasil pembagian: {hasil}")
except ValueError:
    # exception handler untuk nilai yang tidak valid
    print("Input harus berupa angka!")
except ZeroDivisionError:
    # exception handler untuk pembagian dengan nol
    print("Tidak bisa melakukan pembagian dengan nol!")
except Exception as e:
    # exception handler umum
    print(f"Terjadi kesalahan: {e}")
finally:
    # blok kode yang akan selalu dijalankan
    print("Program selesai.")

# Exception Handler dengan konsep OOP

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Jumlah deposit harus lebih dari nol!")
            self.balance += amount
            print(f"Deposit sebesar {amount} berhasil dilakukan. Saldo sekarang: {self.balance}")
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Saldo tidak mencukupi untuk melakukan penarikan!")
            self.balance -= amount
            print(f"Penarikan sebesar {amount} berhasil dilakukan.Saldo sekarang: {self.balance}")
        except ValueError as e:
            print(e)

# membuat objek dari class BankAccount
my_account = BankAccount(1000)

# melakukan deposit sebesar -500 (akan menghasilkan ValueError)
my_account.deposit(-500)

# melakukan deposit sebesar 500 (berhasil)
my_account.deposit(500)

# melakukan penarikan sebesar 1500 (akan menghasilkan ValueError)
my_account.withdraw(1500)

# melakukan penarikan sebesar 500 (berhasil)
my_account.withdraw(500)

# Raise Exception Handler

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    else:
        return a/b
    
try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print(e)
else:
    print("The result is:", result)