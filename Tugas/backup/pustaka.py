def BinarySearch(A,cari):
    idx = []
    found = False
    batasbawah = 0 # left
    batasatas = len(A)-1 # right
    i = 0

    # Algoritma
    while batasbawah <= batasatas and not found:
        mid = (batasatas+batasbawah)//2 # middle
        if A[mid] == cari:
            found = True
            idx.append(i)
        else:
            if A[mid] > cari:
                batasatas = mid-1
            else:
                batasbawah = mid+1
        i = i+1
    if found == True:
        print(cari, 'pada A', found, ', jumlahnya', len(idx),', pada index ', end='')
        print(f'{cari} pada A {found} ,jumlahnya {len(idx)}, pada index ', end='')
        for i in range(len(idx)):
            print(idx[i], end=' ')
    else:
        print('tidak terdapat', cari, 'pada A')

def InsertionSortA(n,A):
    temp = 0
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and temp < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = temp
    return A