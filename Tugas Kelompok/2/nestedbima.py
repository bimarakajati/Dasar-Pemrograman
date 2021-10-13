# Program Menabung

# kamus
batas = int(input('Berapa bulan anda menabung? '))
Tabungan = []

# algoritma
for i in range(0,batas):
    for j in range(0,3):
        Mingguan = int(input('Masukan tabungan minggu ke-{}: ' .format(j+1)))
        Tabungan.append(Mingguan)
    total = sum(Tabungan)
    print('Total tabungan anda pada bulan ke-{}: Rp. {:,}.00\n' .format((i+1),total))
# print(Tabungan)
print('Total semua tabungan anda selama {} bulan: Rp. {:,}.00\n' .format(batas,total))