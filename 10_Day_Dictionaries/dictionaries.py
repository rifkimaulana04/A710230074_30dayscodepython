mahasiswa = {'nama':'Maul','umur':19} 
mahasiswa['umur'] = 19 
mahasiswa['alamat'] = 'Surakarta' 
mahasiswa['angkatan'] = 2024 
print(mahasiswa) 
print(mahasiswa.pop('angkatan')) 
print(mahasiswa) 
print('nama' in mahasiswa) 
print(len(mahasiswa)) 
print(sorted(mahasiswa)) 
mahasiswa.clear() 
print(mahasiswa) 