def LinearSearch(k,n,A):
    # parameter k merupakan bilangan yang dicari, 
    # n merupakan panjang array, A merupakan array
    # Kamus Lokal
    found = False
    # Algoritma
    for i in range(n):
        if A[i] == k:
            found = True
    return found