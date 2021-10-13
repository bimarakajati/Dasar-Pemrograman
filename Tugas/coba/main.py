import pustaka

def main():
    A = [1,5,8,9,20,20,20,20,50]
    print('A =',A)
    B=int(input('Data yang ingin dicari : '))
    pustaka.BinarySearch(A,B)

if __name__ == '__main__':
    main()