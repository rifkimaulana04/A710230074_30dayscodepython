# Membaca dan menulis File

fileku = open("buah.txt","w")
fileku.write('Apel\n')
fileku.write('Mangga\n')
fileku.write('Jambu')
fileku.close()
bacafileku = open("buah.txt","r")
print(bacafileku.read())

# Menambah data pada file

fileku = open("jurusan.txt","w")
fileku.write('Biologi\n')
fileku.write('PGSD\n')
fileku.write('PTI\n')
fileku.close()
with open("jurusan.txt",'a+') as f:
    f.write('Akuntansi\n')
    f.write('PAUD')

with open("jurusan.txt",'r') as baca:
    print(baca.read())

# Attribute pada file

fileku = open("kereta.txt", "w")
fileku.write('Prameks\n')
fileku.write('Joglosemarkerto\n')
fileku.write('Sancaka\n')
fileku.close()
my_file = open("kereta.txt", "a+")
print("Filenamenya adalah : ", my_file.name)
print("File modenya adalah", my_file.mode)
print("Encoding filenya adalah", my_file.encoding)
print("Apakah file sudah ditutup?", my_file.closed)
my_file.close()
print("Apakah file sudah ditutup", my_file.closed)