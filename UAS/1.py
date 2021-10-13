# kamus
n = str(input('Masukkan String : '))

# algoritma
for i in range (len(n)):
    print (' ' * i,end='')
    for j in range(i,len(n)):
        print(n[j],end='')
    print()