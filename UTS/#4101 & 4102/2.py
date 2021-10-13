nm = input('Inputkan nama           = ')
um = int(input('Inputkan umur           = '))
tb = int(input('Inputkan tinggi badan   = '))

print(nm)

if 17 >= um < 30:
    if tb >= 165:
        print('DITERIMA SEBAGAI STAFF ADMINISTRASI')
    else:
        print('TIDAK DITERIMA SEBAGAI PEGAWAI')
elif 30 >= um < 40:
    if tb >= 170:
        print('DITERIMA SEBAGAI KEPALA ADMIN')
    elif 160 >= tb < 170:
        print('DITERIMA SEBAGAI STAFF ADMIN')
    else:
        print('TIDAK DITERIMA SEBAGAI PEGAWAI')
else:
    print('TIDAK DITERIMA SEBAGAI PEGAWAI')
