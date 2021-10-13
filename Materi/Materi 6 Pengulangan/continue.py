#Judul: Menampilkan deret bilangan tanpa 5

#Kamus
N = 0

#Algoritma
Batas = int(input())
while N<Batas:
    N+=1
    if N == 5:
       continue
    print(N)    
print("Selesai")