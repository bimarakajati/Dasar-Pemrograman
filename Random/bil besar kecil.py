# kamus
a = int(input('Masukkan bil a: '))
b = int(input('Masukkan bil b: '))
c = int(input('Masukkan bil c: '))

# algoritma
# menentukan yg terbesar
if b < a > c:
    print('bil a({}) lebih besar dari b({}) dan c({})' .format(a,b,c))
elif a < b > c:
    print('bil b({}) lebih besar dari a({}) dan c({})' .format(b,a,c))
elif b < c > a:
    print('bil c({}) lebih besar dari b({}) dan a({})' .format(c,b,a))
else:
    print('input tidak valid')

# menentukan yg terkecil
if b > a < c:
    print('bil a({}) lebih kecil dari b({}) dan c({})' .format(a,b,c))
elif a > b < c:
    print('bil b({}) lebih kecil dari a({}) dan c({})' .format(b,a,c))
elif b > c < a:
    print('bil c({}) lebih kecil dari b({}) dan a({})' .format(c,b,a))
else:
    print('input tidak valid')