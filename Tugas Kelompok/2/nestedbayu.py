# Program Menentukan Bil Prima

# kamus
batas = int(input('Masukan batas: '))
i = 2

# algoritma
while(i < batas):
    j = 2
    while(j <= (i/j)):
        if (i%j == 0):
            break
        j += 1
    if (j > i/j) : 
        print (i, 'adalah bilangan prima')
    i += 1
print ('Program Selesai!')