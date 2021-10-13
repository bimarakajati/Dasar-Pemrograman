#Judul: Menampilkan deret bilangan hingga 5

#Kamus
N = 1

#Algoritma
Batas = int(input())
while N<=Batas:
    if N > 5:
       break
    print(N)
    N+=1
print('Selesai')
