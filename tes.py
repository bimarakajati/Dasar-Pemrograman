#Judul: Menjumlahkan deret 
# bilangan hingga 3
#Kamus
N = 1
jumlah = 0

#Algoritma
while True:
    print(N)   
    jumlah = jumlah + N
    N+=1
    if N > 3:
       break
print(jumlah)
