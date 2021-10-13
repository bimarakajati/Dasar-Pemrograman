baris = int(input('masukkan jumlah baris : '))
kolom = int(input('masukkan jumlah kolom : '))
xx = int(input('masukkan nilai [1][1] : '))
xy = int(input('masukkan nilai [1][2] : '))
xz = int(input('masukkan nilai [1][3] : '))
yz = int(input('masukkan nilai [2][1] : '))
yy = int(input('masukkan nilai [2][2] : '))
yz = int(input('masukkan nilai [2][3] : '))
zx = int(input('masukkan nilai [3][1] : '))
zy = int(input('masukkan nilai [3][2] : '))
zz = int(input('masukkan nilai [3][3] : '))
ii = int(input('masukkan nilai [4][1] : '))
ij = int(input('masukkan nilai [4][2] : '))
ik = int(input('masukkan nilai [4][3] : '))

matriks = [
   xx,xy,xz,
   yz,yy,yz,
   zx,zy,zz,
   ii,ij,ik
]

print('matriks hasil inputan =')
print(xx,xy,xz)
print(yz,yy,yz)
print(zx,zy,zz)
print(ii,ij,ik)

print('nilai tertinggi kolom ganjil adalah = ', max(matriks))
print('nilai terendah kolom ganjil adalah = ', min(matriks))