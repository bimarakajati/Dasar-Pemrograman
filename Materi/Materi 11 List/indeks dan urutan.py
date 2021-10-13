L = []	# list kosong
L = [2,'a',4,[1,2]]	# list yang berisi elemen2
print(len(L)) # fungsi untuk mengecek banyaknya elemen list sehingga menghasilkan nilai 4
print(L[0]) # Menghasilkan elemen pertama (indeks mulai dari 0) dari List yaitu 2
print(L[2]+1) # Elemen ketiga + 1 sehingga 4+1 menghasilkan nilai 5
print(L[3]) # menghasilkan list yang lain yaitu [1,2] !
# L[4] # Error, karena hanya sampai indeks ke-3
i = 2
print(L[i-1]) # Menghasilkan nilai 'a' karena L[1] = 'a'