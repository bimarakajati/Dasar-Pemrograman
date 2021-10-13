#soal 1

s=""
i=1
while (i<=10) :
    s += str(i) +" "
    i += 1
print(s)

s=""
i=2
while (i<=10) :
    s += str(i) +" "
    i += 2
print(s)

s=""
i=3
while (i<=10) :
    s += str(i) +" "
    i += 3
print(s)

s=""
i=4
while (i<=10) :
    s += str(i) +" "
    i += 4
print(s)
print('no 1')
for n in range (1,11) :
    print(n,end=" ")
print("")
for n in range (1,11) :
    if n%2==0:
        print(n, end=" ")
print("")
for n in range (1,11):
    if n%3==0:
        print(n, end=" ")
print("")
for n in range (1,11):
    if n%4==0:
        print(n,end=" ")
print("")

#soal 2

b = int(input("Masukkan Jumlah Baris: "))
k = int(input("Masukkan Jumlah Kolom: "))
n = int(input("Masukka Jumlah Array {},{}: ".format(b,k)))
for baris in range(0,b):
    for kolom in range(0,k):
        print(n, end=" ")
        n+=1
    print(" ")


#soal 3
print("soal no 3")
# Kode
A = [2,4,7,6,9]
B = [6,9,5,12,7]
print(A[0] + A[3],end=" ")
print(B[0] + B[3])
print((A[0] + A[3] )+(B[0] + B[3]))

#Notasi Algoritmik
# A = {2,4,7,6,9}
# B = {6,9,5,12,7}

# Output(A)
# Output(B)
# Output((A) + (B))

#soal 4

baris = int(input('Masukkan Jumlah Baris : '))
kolom = int(input('Masukkan Jumlah Kolom : '))
n=1
for b in range(0,baris) :
   for k in range(0,kolom) :
      print(n, end=" ")
      n+=1
   print(" ")

print('Nilai tertinggi kolom ganjil adalah = ')
print('Nilai terendah kolom ganjil adalah = ')