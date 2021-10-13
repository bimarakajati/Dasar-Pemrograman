# kamus
nama = input('Masukkan Nama Pembeli : ')
kode = int(input('Masukkan Kode Susu [1/2/3] : '))
ukuran = input('Masukkan Kode Ukuran [S/M/L] : ').lower()
jmlbeli = int(input('Masukkan Jumlah Beli : '))

# algoritma
if kode == 1:
    merk = 'Indomilk'
    if ukuran == 's':
        harga = 5000
    elif ukuran == 'm':
        harga = 7500
    elif ukuran == 'l':
        harga = 9500
    else:
        print('Error, merk yang anda masukkan salah!')
elif kode == 2:
    merk = 'Dancow'
    if ukuran == 's':
        harga = 4500
    elif ukuran == 'm':
        harga = 6500
    elif ukuran == 'l':
        harga = 8500
    else:
        print('Error, merk yang anda masukkan salah!')
elif kode == 3:
    merk = 'Sustagen'
    if ukuran == 's':
        harga = 9500
    elif ukuran == 'm':
        harga = 15500
    elif ukuran == 'l':
        harga = 19500
    else:
        print('Error, merk yang anda masukkan salah!')
else:
    print('Error, kode yang anda masukkan salah!')

# menentukan harga
jmlpembayaran = jmlbeli * harga

# menentukan diskon
if jmlbeli > 25:
    diskon = jmlpembayaran * (5/100)
else:
    diskon = 0

# menghitung pajak
pajak = jmlpembayaran * (10/100)

# menghitung total
total = jmlpembayaran + pajak - diskon

print('\nSTRUK PEMBAYARAN')
print('Nama Pembeli         :', nama.capitalize())
print('Merk Barang          :', merk)
print('Jenis Ukuran         :', ukuran.upper())
print('Jumlah Beli          :', jmlbeli)
print('Harga Barang         :', harga)
print('Jumlah Pembayaran    :', jmlpembayaran)
print('Potongan             :', diskon)
print('Pajak                :', pajak)
print('Total Pembayaran     :', total)