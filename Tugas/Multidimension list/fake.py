# BIMA RAKAJATI
# A11.2020.13088

# program python multi-dimensional list
a = [[0,1,2], [4,5,6,3], [7,8,9,10]] 
print(a)

# fungsi untuk memisahkan/membuat turun kebawah
for i in a: 
	print(i) 

# menghilangkan tanda kurung
for i in range(len(a)) : 
	for j in range(len(a[i])) : 
		print(a[i][j], end=" ") 
	print()

# menambahkan elemen ke kolom terakhir
a.append([11,12,13,14,15]) 
print(a) 

# menggabungkan elemen kedalam kolom pertama
a[2].extend([16,17,18,19,20]) 
print(a)

# membalikkan elemen list
a.reverse() 
print(a)