#kamus
nama = input('Masukkan nama anda: ') # nama
NIK = input('Masukkan NIK anda: ') # nomor induk kepegawaian
status = input('Masukkan status pegawai anda (tetap/honorer): ') # status karyawan
gol = input('Masukkan golongan anda (A/B/C): ') # golongan

#algoritma
if status == 'tetap':
    pokok = 2000000
    if gol == 'A':
        gol = 200000
    if gol == 'B':
        gol = 350000
    if gol == 'C':
        gol = 500000
elif status == 'honorer':
    pokok = 1000000
    if gol == 'A':
        gol = 100000
    if gol == 'B':
        gol = 150000
    if gol == 'C':
        gol = 300000
else:
    print('Input salah')

gaji = pokok + gol
print('\nNama anda {}, NIK {}, Status karyawan {}, Golongan {}' .format(nama,NIK,status,gol))
print('Total gaji anda adalah {}' .format(gaji))
print()