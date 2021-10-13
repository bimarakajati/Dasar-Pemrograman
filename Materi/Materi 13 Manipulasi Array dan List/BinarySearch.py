def BinarySearch(k,n,A):
    # parameter k merupakan bilangan yang dicari, 
    # n merupakan panjang array, A merupakan array
    # Kamus Lokal
    found = False
    batasbawah = 0  #left
    batasatas = n-1    #right
    # Algoritma
    while batasbawah<=batasatas and not found:
        mid = (batasatas+batasbawah)//2     #middle
        if A[mid] == k:
            found = True
        else:
            if A[mid] > k:
                batasatas = mid-1
            else:
                batasbawah = mid+1
    return found