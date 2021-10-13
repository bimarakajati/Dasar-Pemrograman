# kamus
nama = input('Masukkan nama : ')
ipk = float(input('Masukkan IPK : '))
if ipk < 2.75:
    quit()
akreditasi = input('Masukkan akreditasi universitas : ')
if akreditasi == 'A':
    print()
else:
    quit()
akademik = int(input('Masukkan Tes Akademik : '))
ketrampilan = int(input('Masukkan Tes Ketrampilan : '))
psikologi = int(input('Masukkan Tes Psikologi : '))
# algoritma
rata_rata = (akademik + ketrampilan + psikologi) / 3
print('Nilai rata-rata  =', rata_rata)
# menentukan bagian yang akan ditempati
if psikologi < akademik > ketrampilan:
    bagian = 'manajemen'
elif psikologi < ketrampilan > akademik:
    bagian = 'produksi'
else:
    bagian = 'pemasaran'
# menentukan lulus/tidak
if akademik < 80:
    print('Mohon Maaf {} anda tidak diterima, karena ada nilai Tes dibawah 80' .format(nama))
if ketrampilan < 80:
    print('Mohon Maaf {} anda tidak diterima, karena ada nilai Tes dibawah 80' .format(nama))
if psikologi < 80:
    print('Mohon Maaf {} anda tidak diterima, karena ada nilai Tes dibawah 80' .format(nama))
elif rata_rata >= 80:
    print('Selamat {} anda Diterima, dan ditempatkan di {}' .format(nama, bagian))
else:
    print('Mohon Maaf {} anda tidak diterima, karena rata-rata Tes dibawah 80' .format(nama))