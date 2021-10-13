# Program Pola Setengah Segitiga

# kamus
a = int(input('Batas Akhir: '))
s = 2 * a - 2 

# algoritma
for i in range(0, a):
    for j in range (0, s):
        print(' ',end='')
    s -= 2
    
    for j in range (0, i + 1):
        print('* ' , end='')
    print('')