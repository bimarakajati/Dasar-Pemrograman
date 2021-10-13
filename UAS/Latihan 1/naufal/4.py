list_num = [77,48,2,23,33,45,56,0,86,71]
cari = int(input('data yg dicari: '))
print(*[f'data ditemukan pada indeks {list_num.index(cari)}.' if cari in list_num else 'data tidak diketahui'])