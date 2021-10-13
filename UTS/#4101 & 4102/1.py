bil1 = int(input('Bilangan 1    = '))
bil2 = int(input('Bilangan 2    = '))
bil3 = int(input('Bilangan 3    = '))

hasil1 = bil1 * 4
hasil2 = bil2 / 2
hasil3 = bil3 + 20

print('Bilangan 1 menjadi   =', hasil1)
print('Bilangan 2 menjadi   =', hasil2)
print('Bilangan 3 menjadi   =', hasil3)

if hasil2 < hasil1 > hasil3:
    print('Bilangan terbesar yaitu bilangan 1 sebesar', hasil1)
elif hasil1 < hasil2 > hasil3:
    print('Bilangan terbesar yaitu bilangan 2 sebesar', hasil2)
else:
    print('Bilangan terbesar yaitu bilangan 3 sebesar', hasil3)

if hasil2 > hasil1 < hasil3:
    print('Bilangan terbesar yaitu bilangan 1 sebesar', hasil1)
elif hasil1 > hasil2 < hasil3:
    print('Bilangan terbesar yaitu bilangan 2 sebesar', hasil2)
else:
    print('Bilangan terbesar yaitu bilangan 3 sebesar', hasil3)