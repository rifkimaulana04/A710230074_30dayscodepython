# Single Responsibility Principle (SRP)

# Misalkan kita memiliki kelas UserManager yang bertanggung jawab untuk  mengelola data pengguna dan juga mencetak laporan pengguna. Ini melanggar SRP  karena UserManager memiliki lebih dari satu tanggung jawab.
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
    
    def print_user_report(self):
        for user in self.users:
            print(f'User: {user.name}, Email: {user.email}')

# Untuk mematuhi SRP, kita bisa memindahkan tanggung jawab mencetak laporan ke kelas lain, seperti UserReport. 
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class UserReport:
    @staticmethod
    def print_user_report(users):
        for user in users:
            print(f'User: {user.name}, Email: {user.email}')


# Membuat objek User
user1 = User('Alice', 'alice@example.com')
user2 = User('Bob', 'bob@example.com')

# Membuat objek UserManager dan menambahkan User
user_manager = UserManager()
user_manager.add_user(user1)
user_manager.add_user(user2)

# Membuat objek UserReport dan mencetak laporan
user_report = UserReport()
user_report.print_user_report(user_manager.users)

# Open/Closed Principle (OCP)

# Misalkan kita memiliki program yang mencetak pesan selamat datang dalam berbagai bahasa. Dalam contoh ini, jika kita ingin menambahkan bahasa baru, kita harus memodifikasi metode greet pada kelas Greeter. Ini melanggar Prinsip Open/Closed Principle (OCP) karena kita harus memodifikasi kelas yang ada untuk menambahkan fungsi baru. 
class Greeter:
    def __init__(self, language):
        self.language = language
    
    def greet(self):
        if self.language == 'english':
            return 'Hello!'   
        elif self.language == 'spanish':
            return '¡Hola!'  
        elif self.language == 'french':
            return 'Bonjour!'
        else:
            return 'Language not supported.'
        
# Untuk mematuhi Prinsip Open/Closed Principle (OCP), kita bisa merancang kelas Greeter agar dapat menerima objek "Greeting" yang dapat menyapa dalam bahasa apa pun, seperti ini:
class Greeter:
    def __init__(self, greeter):
        self.greeter = greeter
    
    def greet(self):
        return self.greeter.greet()

class EnglishGreeter:
    def greet(self):
        return 'Hello!'


class SpanishGreeter:
    def greet(self):
        return '¡Hola!'


class FrenchGreeter:
    def greet(self):
        return 'Bonjour!'


# Membuat objek greeter dalam berbagai bahasa
english_greeter = EnglishGreeter()
spanish_greeter = SpanishGreeter()
french_greeter = FrenchGreeter()

# Membuat objek Greeter dan menggreet dalam berbagai bahasa
greeter = Greeter(english_greeter)
print(greeter.greet()) # Output: Hello!

greeter = Greeter(spanish_greeter)
print(greeter.greet()) # Output: ¡Hola!

greeter = Greeter(french_greeter)
print(greeter.greet()) # Output: Bonjour!

# Open/Closed Principle (OCP)

# Perhatikan contoh kode berikut, Ostrich adalah turunan dari Bird, namun Ostrich tidak dapat terbang seperti Bird lainnya. Ini melanggar Liskov Substitution Principle karena kita tidak bisa menggantikan Bird dengan Ostrich dalam konteks terbang.
class Bird:
    def fly(self):
        return "I can fly!"

class Duck(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
        return "I can't fly!"

# Untuk mematuhi Liskov Substitution Principle, kita bisa mendefinisikan ulang hirarki kelas kita. Kita bisa membuat kelas FlyingBird dan NonFlyingBird yang merupakan turunan dari Bird, dan memindahkan metode fly ke FlyingBird.

class Bird:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, I'm a {self.name}."

class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"


class NonFlyingBird(Bird):
    def walk(self):
        return "I can walk!"


class Duck(FlyingBird):
    def quack(self):
        return "Quack!"


class Ostrich(NonFlyingBird):
    def run(self):
        return "I can run fast!"
 
# Membuat objek Duck dan Ostrich
duck = Duck("Duck")
ostrich = Ostrich("Ostrich")

# Duck bisa terbang dan berbunyi "quack"
print(duck.introduce()) # Output: Hello, I'm a Duck.
print(duck.fly()) # Output: I can fly!
print(duck.quack()) # Output: Quack!

# Ostrich tidak bisa terbang, dan bisa berjalan dan berlari cepat
print(ostrich.introduce()) # Output: Hello, I'm an Ostrich.
print(ostrich.walk()) # Output: I can walk!
print(ostrich.run()) # Output: I can run fast!