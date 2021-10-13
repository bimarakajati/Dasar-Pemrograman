provider = input('Nama Provider      : ')
no = input('Nomor Telp         : ')
jam = int(input('Durasi Jam         : '))
menit = int(input('Durasi Menit       : '))
detik = int(input('Durasi Detik       : '))
saldo = int(input('Saldo Pulsa        : '))

totaldetik = (jam*60*60) + (menit*60) + detik
biaya = (totaldetik/30) * 1000
if 10000 >= biaya < 20000:
    bonus = 1000
elif 20000 >= biaya < 40000:
    bonus = 5000
elif biaya >= 40000:
    bonus = 10000
saldo_akhir = saldo - (biaya-bonus)

print('Nama Provider            :', provider)
print('Nomor Telp               :', no)
print('Ubah Jam+Menit+Detik     : {} detik' .format(totaldetik))
print('Total Pengeluaran Pulsa  : {} Rupiah' .format(biaya))
print('Bonus Pulsa              : {} Rupiah' .format(bonus))
print('Saldo Pulsa Sekarang     :', saldo_akhir)