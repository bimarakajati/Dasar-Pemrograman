# Menentukan predikat kelulusan berdasarkan IPK mahasiswa
# Kamus
ipk = 0.0 # ipk bertipe float
ipk = float(input('Masukkan IPK: '))

#algoritma
if ipk >= 3.5:
    print('Dengan pujian/Cumlaude')
elif 3.0 <= ipk < 3.5:
    print('Sangat memuaskan/Very Good')
else:
    print('Memuaskan/Good')