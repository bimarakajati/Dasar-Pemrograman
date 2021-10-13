NMin = 1
NMax = 10
T = [int]*NMax
x = 0
i = NMin
x = int(input())
while x != 9999 and i<NMax:
    T[i] = x
    i = i + 1
    x = int(input())
    if x==9999:
        break
if i>NMax:
    print("array penuh")
for j in range(NMin-1,i+1):
    print(T[j])
