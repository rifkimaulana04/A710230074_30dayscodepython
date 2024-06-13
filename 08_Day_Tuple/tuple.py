truk = ('hino', 3000, 2.5 , 130 ) 
merk, cc , berat , top_speed = truk 
print(truk[0]) 
print(truk[:2]) 
print(truk[2:]) 
print(truk.index(3000)) 
print(2.5 in truk) 
print('truk {} memiliki berat {} ton, kapasitas {} cc dan top speed {} km/jam'.format(merk,berat,cc,top_speed))