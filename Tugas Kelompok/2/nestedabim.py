# Program Deret Angka

# kamus
x = int(input('Batas Akhir: '))

# algoritma
for i in range (1,x+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()