# kamus
a = [] # list kosong

print('Masukkan 10 Data Bilangan bulat :')
for i in range(10): # looping input 10x
    r = int(input('Bilangan {} = '.format(i+1)))
    a.append(r) # hasil input ditambahkan ke list a
b = sum(a)/10 # rata-rata
print('Rata-rata = ', b)
for j in a: # mencari daftar nilai diatas rata-rata
    if j > b:
        print(j)