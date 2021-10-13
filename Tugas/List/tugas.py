# Bima Rakajati
# A11.2020.13088

# list 
fakultas = ['Ilmu Komputer', 'Teknik', 'Ekonomi']
nim = ['A11.2020.13088', 'A11.2020.13089']
nim2 = ['A11.2020.13090', 'A11.2020.13091']
nama = []

fakultas.append('Kesehatan')
print(fakultas)
fakultas.remove('Teknik')
print(fakultas)
print('Fakultas pertama adalah {} '.format(fakultas[0]))
print('Ada {} fakultas di udinus, yaitu:'.format(len(fakultas)))
for x in fakultas:
    print(x)

nama.append('Bima')
nama.insert(0, 'Raka')
print(nama)

nim.extend(nim2)
print(nim)
print('NIM {} adalah {}'.format(nama[0], nim[0]))
nim = nim + nim2
print(nim)