# Kasus 5
n = int(input("Masukkan jumlah n: "))
a = []
b = []
for i in range(n):
    a.append([])
    b.append([])

for j in range(n):
    bil = int(input("Bilangan A {}: ".format(j+1)))
    a[i].append(bil)
for j in range(n):
    bil = int(input("Bilangan B {}: ".format(j+1)))
    b[i].append(bil)

print(*a[i])
print(*b[i])

c = set(a[i])
d = set(b[i]) #Set berfungsi sebagai pengubah menjadi {}

e = c & d
print("Nilai Nilai Yang Berisan Pada List A dan List B:",*e)
print(sum(e))