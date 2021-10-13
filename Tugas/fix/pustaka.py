def BinarySearch(A,cari):
    idx = []
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
    for i in range(len(A)):
        if A[i] == cari:
            idx.append(i)
    if found == True:
        print(cari, "Pada A {}, jumlahnya {} terdapat pada index".format(found,len(idx)),end=" ")
        for i in range(len(idx)):
            print(idx[i],end=" ")
    else:
        print("index tidak tersedia pada list")