# kamus
a = int(input('Masukkan batas akhir : '))
b=1
# algoritma
for i in range (1, a, 1):
    for j in range (1, i):
        print(j, end='')
        b+=1
    print()