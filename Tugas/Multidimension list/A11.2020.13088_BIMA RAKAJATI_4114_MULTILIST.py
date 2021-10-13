# BIMA RAKAJATI
# A11.2020.13088
# 4114

# Program python untuk ngeprint list multi-dimensi
x = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15]
] 
print(*x)

for i in x: 
	print(i) 

# nge-print semua elemen dalam var x 
# dengan bantuan looping for
for i in range(len(x)) : 
	for j in range(len(x[i])) : 
		print(x[i][j], end=" ") 
	print()

# menambahkan data kedalam list 
# menggunakan fungsi append
x.append([21, 22, 23, 24, 25]) 
print(x) 

# memperpanjang elemen list
# menggunakan fungsi extend
x[2].extend([16, 17, 18, 19, 20]) 
print(x)

# membalikkan data list
# menggunakan fungsi reverse
x.reverse() 
print(x) 
x[0].reverse() 
print(x) 

# menghapus data list
# menggunakan fungsi remove
x.remove([25, 24, 23, 22, 21])
print(x) 