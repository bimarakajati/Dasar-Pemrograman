a = int(input('Masukkan angka :'))
b=1
for i in range (0, a, 1):
    for j in range (0, i):
        print(j, end='')
        b+=1
    print()
for i in range (a, 0, -1):
    for j in range (0, i):
        print(j, end='')
        b+=1
    print()