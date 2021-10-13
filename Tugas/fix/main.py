import pustaka

# entry point dengan prosedur main
def main():
    A = [1,5,8,9,20,20,20,20,50]
    print('A =',A)
    c=int(input('Data yang ingin dicari : '))
    pustaka.BinarySearch(A,c)

# panggil entry point
if __name__ == '__main__':
    main()