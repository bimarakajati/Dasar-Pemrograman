print("nomor 4\n")
bil=[]
for i in range(10):
    bilangan=int(input("bilangan {}=".format(i+1)))
    bil.append(bilangan)
hasil=sorted(bil)

print("hasil setelah diurutkan= ",end="")
for j in range(max(hasil)+1):
    if j in hasil:
        print(j, end="")