# kamus
n = int(input("Masukkan jumlah n: "))
a = []
b = []

# algoritma
for i in range(n):
    a.append([])
    b.append([])

for j in range(n):
    bil = int(input("Bilangan A {}: ".format(j+1)))
    a[i].append(bil)
for j in range(n):
    bil = int(input("Bilangan B {}: ".format(j+1)))
    b[i].append(bil)

print(a[i])
print(b[i])

c = set(a[i])
d = set(b[i]) # mengubah list menjadi string

e = c & d
f = list(e)
print("Nilai Nilai Yang Berisan Pada List A dan List B:",f)
genap = []
ganjil = []
for i in range(len(f)):
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)
print('Jumlah nilai-nilai beririsan yang genap saja', *genap, '=', sum(genap))
print('Jumlah nilai-nilai beririsan yang ganjil saja', *ganjil, '=', sum(ganjil))
total = sum(genap) + sum(ganjil)
print('Total genap+ganjil = ', sum(genap), '+', sum(ganjil) ,'=', total)