def BinarySearch(A,cari):
    idx = [] # list kosong
    found = False
    batasbawah = 0 # left
    batasatas = len(A)-1 # right

    # Algoritma
    while batasbawah <= batasatas and not found:
        mid = (batasatas+batasbawah)//2 # middle
        if A[mid] == cari:
            found = True
        else:
            if A[mid] > cari:
                batasatas = mid-1
            else:
                batasbawah = mid+1
    for x in range(len(A)): # mencari index
        if A[x] == cari:
            idx.append(x)
    if found == True:
        print(f'{cari} pada A = {found}, jumlahnya {len(idx)}, terdapat pada index ', end='')
        for y in range(len(idx)):
            print(idx[y], end=' ')
    else:
        print(f'Tidak terdapat {cari} pada A')