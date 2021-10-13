#kamus
n = int(input('Masukkan angka: '))
sum = 0
i = 1
#algoritma
while i <= n:
    print(i)
    sum = sum + i
    i = i + 1
print('hasil penjumlahan dari 1 sampai '+str(n), ' adalah '+str(sum))