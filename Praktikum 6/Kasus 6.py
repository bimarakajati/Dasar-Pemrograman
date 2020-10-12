#kamus
saldo = int(input('Saldo awal: '))
sisa = saldo
#algoritma
while True:
    n = int(input('Pengeluaran soni hari ini (isikan -1 untuk keluar): '))
    if n == -1:
        print('sisa saldo', sisa)
        break
    sisa = sisa - n
    if sisa < 0:
        print('saldo tidak cukup')
        print('sisa saldo', sisa+n)
        break