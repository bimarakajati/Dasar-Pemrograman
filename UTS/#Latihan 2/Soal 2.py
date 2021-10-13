# program sederhana untuk menampilkan array 2 dimensi
# kamus
baris = int(input('Masukkan Jumlah Baris : '))
kolom = int(input('Masukkan Jumlah Kolom : '))
# algoritma
n=1
print('Array 1 :')
for b in range(0,baris) :
   for k in range(0,kolom) :
      print(n, end=" ")
      n+=1
   print(" ")