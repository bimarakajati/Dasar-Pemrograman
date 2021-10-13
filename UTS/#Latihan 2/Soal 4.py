# program untuk menyimpan nilai-nilai dalam sebuah array dua dimensi
# kamus
baris = int(input('Masukkan jumlah baris : '))
kolom = int(input('Masukkan jumlah kolom : '))
aa = int(input('Masukkan nilai [1][1] : '))
ab = int(input('Masukkan nilai [1][2] : '))
ac = int(input('Masukkan nilai [1][3] : '))
ba = int(input('Masukkan nilai [2][1] : '))
bb = int(input('Masukkan nilai [2][2] : '))
bc = int(input('Masukkan nilai [2][3] : '))
ca = int(input('Masukkan nilai [3][1] : '))
cb = int(input('Masukkan nilai [3][2] : '))
cc = int(input('Masukkan nilai [3][3] : '))
da = int(input('Masukkan nilai [4][1] : '))
db = int(input('Masukkan nilai [4][2] : '))
dc = int(input('Masukkan nilai [4][3] : '))

matriks = [
   aa,ab,ac,
   ba,bb,bc,
   ca,cb,cc,
   da,db,dc
]

print('Matriks hasil inputan =')
print(aa,ab,ac)
print(ba,bb,bc)
print(ca,cb,cc)
print(da,db,dc)

print('Nilai tertinggi kolom ganjil adalah = ', max(matriks))
print('Nilai terendah kolom ganjil adalah = ', min(matriks))