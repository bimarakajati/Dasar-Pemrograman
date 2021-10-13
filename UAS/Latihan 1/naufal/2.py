bulan = [
    'Januari', 'Februari', 'Maret', 'April',
    'Mei', 'Juni', 'Juli', 'Agustus', 
    'September', 'Oktober', 'November', 'Desember'
]
# print(f'penentuan nama bulan\n{'-'*22}')
bulan_apa = int(input('kode bulan (1..12): '))
if 0 < bulan_apa <= 12:
    print(f'bulan {bulan[bulan_apa-1]}')
else:
    print('kode bulan harus antara 1-12')