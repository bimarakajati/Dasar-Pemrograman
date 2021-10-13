# Menentukan predikat berdasarkan nilai

# Kamus
nilai = 0 
nilai = int(input('Masukkan Nilai (0-100): ')) # Nilai bertipe integer

#algoritma
if nilai >= 90:
    print('Anda mendapatkan predikat A')
elif 80 <= nilai < 90:
    print('Anda mendapatkan predikat B')
elif 70 <= nilai < 80:
    print('Anda mendapatkan predikat C')
elif 60 <= nilai < 70:
    print('Anda mendapatkan predikat D')
else:
    print('Anda mendapatkan predikat E')