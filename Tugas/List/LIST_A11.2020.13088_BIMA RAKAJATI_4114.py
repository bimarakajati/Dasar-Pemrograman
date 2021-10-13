# Bima Rakajati
# A11.2020.13088

# list fakultas
fakultas = ['Ilmu Komputer', 'Teknik', 'Ekonomi']

fakultas.append('Kesehatan') # menambahkan kesehatan ke list fakultas
print(fakultas)
fakultas.remove('Teknik') # menghapus teknik dari list fakultas
print(fakultas)
print('Fakultas pertama adalah {} '.format(fakultas[0]))
print('Ada {} fakultas di udinus, yaitu:'.format(len(fakultas))) # menghitung panjang list dengan len
for x in fakultas: # ngeprint elemen2 yg ada di list
    print(x)
print('Fakultas ke 3 adalah {} '.format(fakultas[2])) # menampilkan indeks ke 2 dari list

# list nama
nama = ['Bayu', 'Nadia', 'Abi']

nama.insert(0, 'Bima Rakajati') # menambahkan Bima Rakajati di index 0 dari list nama
print(nama)
print('Ada {} mahasiswa di udinus, yaitu:'.format(len(nama))) # menghitung panjang list dengan len
for x in nama: # ngeprint elemen2 yg ada di list
    print(x)

#list nim
nim = ['A11.2020.13088', 'A11.2020.13089']
nim2 = ['A11.2020.13090', 'A11.2020.13091']

nim.extend(nim2) # menggabungkan list nim dengan nim2
print(nim)
print('NIM {} adalah {}'.format(nama[0], nim[0])) # menampilkan elemen dari list yg berbeda
print(nim[2:]) # memotong list

#list matkul
matkul = ['kalkulus', 'fisika']
matkul_fav = ['daspro', 'daskom']

mata_kuliah = matkul + matkul_fav # menggabungkan list dengan operasi +
print(mata_kuliah)

# list program studi dengan 2 dimensi
progdi = [
    ['Teknik', 'Informatika'],
    ['Sistem', 'Informatika'],
    ['Desain', 'Komunikasi', 'Visual']
]

print(progdi[1])