# kamus
a = [ # list bulan
    'Januari',
    'Februari',
    'Maret',
    'April',
    'Mei',
    'Juni',
    'Juli',
    'Agustus',
    'September',
    'Oktober',
    'November',
    'Desember',
]
print('Penentuan Nama Bulan')
print('----------------------------------')

# algoritma
x = int(input('Kode bulan (1..12): ')) # input kode
if 0 < x <= 12: # apabila input 1-12 maka akan dilanjut ke kode selanjutnya
    if x==1:
        print('Bulan', a[0])
    elif x==2:
        print('Bulan', a[1])
    elif x==3:
        print('Bulan', a[2])
    elif x==4:
        print('Bulan', a[3])
    elif x==5:
        print('Bulan', a[4])
    elif x==6:
        print('Bulan', a[5])
    elif x==7:
        print('Bulan', a[6])
    elif x==8:
        print('Bulan', a[7])
    elif x==9:
        print('Bulan', a[8])
    elif x==10:
        print('Bulan', a[9])
    elif x==11:
        print('Bulan', a[10])
    else:
        print('Bulan', a[11])
else: # apabila input kurang atau lebih dari 1-12
    print('Kode bulan harus antara 1 sampai 12')