nilai = [7,8,9,1,4,0,3,5,2,6]
for i in range(len(nilai)):
    if i % 2 == 0:
        print(nilai[i+1], end=' ')
    else:
        print(nilai[i-1], end=' ')
print()