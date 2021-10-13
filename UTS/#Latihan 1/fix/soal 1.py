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

# algoritma
print('Pilih Operasi')
print('Ket: (1) Penjumlahan (2) Pengurangan')
operasi1 = int(input('Pilih Operasi ke-1 = '))
operasi2 = int(input('Pilih Operasi ke-2 = '))

if operasi1 == 1: # penjumlahan
    if operasi2 == 1: # penjumlahan dan penjumlahan
        hasil = nilai1 + nilai2 + nilai3
        if hasil > 0:
            if hasil % 2 == 0:
                print('Hasil : {} + {} + {} = {} (Bilangan Genap Positif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} + {} + {} = {} (Bilangan Ganjil Positif)' .format(nilai1,nilai2,nilai3,hasil))
        else: 
            if hasil % 2 == 0:
                print('Hasil : {} + {} + {} = {} (Bilangan Genap Negatif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} + {} + {} = {} (Bilangan Ganjil Negatif)' .format(nilai1,nilai2,nilai3,hasil))
    elif operasi2 == 2: # penjumlahan dan pengurangan
        hasil = nilai1 + nilai2 - nilai3
        if hasil > 0:
            if hasil % 2 == 0:
                print('Hasil : {} + {} - {} = {} (Bilangan Genap Positif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} + {} - {} = {} (Bilangan Ganjil Positif)' .format(nilai1,nilai2,nilai3,hasil))
        else:
            if hasil % 2 == 0:
                print('Hasil : {} + {} - {} = {} (Bilangan Genap Negatif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} + {} - {} = {} (Bilangan Ganjil Negatif)' .format(nilai1,nilai2,nilai3,hasil))
elif operasi1 == 2: # pengurangan
    if operasi2 == 1: # penjumlahan dan penjumlahan
        hasil = nilai1 - nilai2 + nilai3
        if hasil > 0:
            if hasil % 2 == 0:
                print('Hasil : {} - {} + {} = {} (Bilangan Genap Positif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} - {} + {} = {} (Bilangan Ganjil Positif)' .format(nilai1,nilai2,nilai3,hasil))
        else:
            if hasil % 2 == 0:
                print('Hasil : {} - {} + {} = {} (Bilangan Genap Negatif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} - {} + {} = {} (Bilangan Ganjil Negatif)' .format(nilai1,nilai2,nilai3,hasil))
    elif operasi2 == 2: # pengurangan dan pengurangan
        hasil = nilai1 - nilai2 - nilai3
        if hasil > 0:
            if hasil % 2 == 0:
                print('Hasil : {} - {} - {} = {} (Bilangan Genap Positif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} - {} - {} = {} (Bilangan Ganjil Positif)' .format(nilai1,nilai2,nilai3,hasil))
        else:
            if hasil % 2 == 0:
                print('Hasil : {} - {} - {} = {} (Bilangan Genap Negatif)' .format(nilai1,nilai2,nilai3,hasil))
            else:
                print('Hasil : {} - {} - {} = {} (Bilangan Ganjil Negatif)' .format(nilai1,nilai2,nilai3,hasil))