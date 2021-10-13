# kamus
daftar = [77, 48, 2, 23, 33, 45, 56, 0, 86, 71] # list data

# algoritma
cari = int(input('Data Yang Dicari : ')) # input data yg dicari
for i in daftar: # loop untuk mencari data di dalam list
    if cari == i: # apabila data ditemukan maka input = True
        ketemu = True
        break
    else: # apabila tidak input = False
        ketemu = False
if ketemu==True: # mencari index pada list
    k=daftar.index(i)
    print('Data Ditemukan pada indeks {}.'.format(k))
else:
    print('Data Tidak Ditemukan.')