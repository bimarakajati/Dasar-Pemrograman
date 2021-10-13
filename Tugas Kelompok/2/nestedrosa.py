# Program Pola Setengah Segitiga Terbalik

# kamus
a = int(input('Inputkan batas: '))
s = 0 # for space

# algoritma
for i in range(0, a):
    for j in range (0, s):
        print(' ',end='')
    s += 2

    for j in range (0, a):
        print('* ' , end='')
    a -= 1
    print('')