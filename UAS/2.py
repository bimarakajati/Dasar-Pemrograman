# kamus 
n = int(input('Masukkan jumlah data = '))
list_num = []

# algoritma
for i in range(n):
    nilai = int(input("Masukkan data ke-{} = ".format(i+1)))
    list_num.append(nilai)

cari = int(input('Masukkan Data Yang Dicari : '))
print(*[f'Data {cari} ditemukan pada indeks {list_num.index(cari)}.' if cari in list_num else 'Data Tidak Ditemukan.'])