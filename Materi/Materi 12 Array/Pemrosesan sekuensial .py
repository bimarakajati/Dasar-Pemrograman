i = 0
NMin = 0
NMax = 100
T = [int]*NMax
N = 0
while True:
    N = int(input())
    if N >= NMin and N <= NMax:
        break
for i in range(NMin,N):
    T[i] = int(input())
for i in range(NMin,N):
    print(T[i])
