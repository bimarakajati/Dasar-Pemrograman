# Kamus
umur = 0 
umur = int(input('Masukkan umur (1-55): ')) # Nilai bertipe integer

#algoritma
if umur <= 5:
    print('Anda mendapatkan kelompok balita')
elif 5 < umur <= 13:
    print('Anda mendapatkan kelompok anak-anak')
elif 13 < umur <= 25:
    print('Anda mendapatkan kelompok remaja')
elif 25 < umur <= 35:
    print('Anda mendapatkan kelompok dewasa')
elif 35 < umur <= 55:
    print('Anda mendapatkan kelompok orangtua')
else:
    print('Anda mendapatkan kelompok umur panjang')