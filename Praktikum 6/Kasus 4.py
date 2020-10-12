#kamus
sum = 0
i = 0
a = int(input('Masukkan angka: '))
#algoritma
while True:
    n = float(input('Masukkan angka: '))
    sum = sum + n
    i = i + 1
    if i >= a:
        rata2 = sum / i
        break
print(int(rata2))