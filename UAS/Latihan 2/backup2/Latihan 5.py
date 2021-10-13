n = int(input('masukkan jumlah n : '))
a = []
b = []

print('masukan nilai-nilai list a dan b')
print('masukan nilai-nilai list a dan b')
for i in range(n):
    nilai=int(input("nilai a {} = ".format(i+1)))
    a.append(nilai)
for j in range(n):
    nilai=int(input("nilai b {} = ".format(j+1)))
    b.append(nilai)
print('A : ', a)
print('B : ', b)