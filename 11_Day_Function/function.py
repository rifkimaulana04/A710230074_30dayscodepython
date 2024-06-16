    # Fungsi dengan parameter

def greet(name, msg='Selamat Pagi'): 
    print("Halo", name + ', ' + msg) 


greet("Batman") 
greet("Robin", "Mau pergi kemana?") 

    # Fungsi dengan parameter list

def maks(a): 
    m = a[0] 
    for i in a: 
        if m < i: 
            m = i 

    return m 

print(maks([5, 2, 1, 4])) 

    #Modul pada python

from math import log10, factorial 

print(log10(100)) 
print(factorial(4)) 

import math 

print(math.pow(5, 2)) 
print(math.sqrt(25))