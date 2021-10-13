# kamus
Array_A = []
Array_B = []
n = int(input('Masukkan Batas Array : '))
# algoritma
for x in range(n):
    A = int(input('Array A ke-{} : ' .format(x+1)))
    Array_A.append(A)
for y in range(n):
    B = int(input('Array B ke-{} : ' .format(y+1)))
    Array_B.append(B)
# list array A dan B
print('Array A  :', Array_A)
print('Array B  :', Array_B)
# hasil penjumlahan array
hasil1 = (Array_A[1] + Array_B[1])
hasil2 = (Array_A[3] + Array_B[3])
print('Hasil    :', hasil1, hasil2)
# total hasil arrat
total = hasil1+hasil2
print('Total    :', total)
# menentukan apabila bilangan kelipatan 6
if total % 6 == 0:
    print('Nilai Total merupakan bilangan kelipatan 6')
else:
    print('Nilai Total bukan merupakan bilangan kelipatan 6')