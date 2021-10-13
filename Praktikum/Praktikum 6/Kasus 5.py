#kamus
bil = int(input('Masukkan bilangan: '))
#algoritma
if bil > 1:
    for i in range(2,bil):
        if (bil % i) == 0:
            print('Bukan bil. prima')
            break
        else:
            print('Bil. prima')
else:
    print('Bukan bil. prima')