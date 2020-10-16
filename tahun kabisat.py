# Menentukan tahun kabisat

tahun = int(input('Masukan tahun: '))

if (tahun % 4) == 0: # Jika angka tahun itu tidak habis dibagi 400, tidak habis dibagi 100 akan tetapi habis dibagi 4, maka tahun itu merupakan tahun kabisat.
    if (tahun % 100) == 0: # Jika angka tahun itu tidak habis dibagi 400 tetapi habis dibagi 100, maka tahun itu sudah pasti bukan merupakan tahun kabisat.
        if (tahun % 400) == 0: # Jika angka tahun itu habis dibagi 400, maka tahun itu sudah pasti tahun kabisat.
            print(tahun, 'adalah tahun kabisat')
        else:
            print(tahun, 'bukan tahun kabisat')
    else:
        print(tahun, 'adalah tahun kabisat')
else:
    print(tahun, 'bukan tahun kabisat')