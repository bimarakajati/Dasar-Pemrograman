# kamus
nilai1 = int(input('Masukkan nilai 1 = '))
if nilai1 > 100: # jika nilai lebih dari 100 program akan keluar
    print('Input maksimal adalah 100! Program berhenti')
    quit()

nilai2 = int(input('Masukkan nilai 2 = '))
if nilai2 > 100: # jika nilai lebih dari 100 program akan keluar
    print('Input maksimal adalah 100! Program berhenti')
    quit()
    
nilai3 = int(input('Masukkan nilai 3 = '))
if nilai3 > 100: # jika nilai lebih dari 100 program akan keluar
    print('Input maksimal adalah 100! Program berhenti')
    quit()

# menu operasi
print('Pilih Operasi')
print('Ket: (1) Penjumlahan (2) Pengurangan')
operasi1 = int(input('Pilih Operasi ke-1 = '))
operasi2 = int(input('Pilih Operasi ke-2 = '))

# algoritma
if operasi1 == 1: # penjumlahan
    op1 = '+'
    if operasi2 == 1: # penjumlahan dan penjumlahan
        op2 = '+'
        hasil = nilai1 + nilai2 + nilai3
    elif operasi2 == 2: # penjumlahan dan pengurangan
        op2 = '-'
        hasil = nilai1 + nilai2 - nilai3
elif operasi1 == 2: # pengurangan
    op1 = '-'
    if operasi2 == 1: # pengurangan dan penjumlahan
        op2 = '+'
        hasil = nilai1 - nilai2 + nilai3
    elif operasi2 == 2: # pengurangan dan pengurangan
        op2 = '-'
        hasil = nilai1 - nilai2 - nilai3

if hasil > 0: # cek bilangan positif
    if hasil % 2 == 0: # cek bilangan genap
        print('Hasil : {} {} {} {} {} = {} (Bilangan Genap Positif)' .format(nilai1,op1,nilai2,op2,nilai3,hasil))
    else: # cek bilangan ganjil
        print('Hasil : {} {} {} {} {} = {} (Bilangan Ganjil Positif)' .format(nilai1,op1,nilai2,op2,nilai3,hasil))
elif hasil < 0: # cek bilangan negatif
    if hasil % 2 == 0: # cek bilangan genap
        print('Hasil : {} {} {} {} {} = {} (Bilangan Genap Negatif)' .format(nilai1,op1,nilai2,op2,nilai3,hasil))
    else: # cek bilangan ganjil
        print('Hasil : {} {} {} {} {} = {} (Bilangan Ganjil Negatif)' .format(nilai1,op1,nilai2,op2,nilai3,hasil))