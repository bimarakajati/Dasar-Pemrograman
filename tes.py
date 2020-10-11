#Kamus
x = 0
x = int(input('masukkan angka: '))

""" #else if
if x > 0:
    print("positif")
elif x < 0:
    print("negatif")
else:
    print("nol") """

#nested if
if x > 0:
    if x % 2 == 0:
        print('genap')
    else:
        print('ganjil')
else:
    print('bukan bil positif')