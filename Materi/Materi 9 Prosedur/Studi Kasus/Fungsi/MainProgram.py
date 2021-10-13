import Voltase		

def main():
    #kamus
    R = int(input())
    A = int(input())	
    #algoritma
    v = Voltase.HitungVoltase(R,A)
    print(v)
if __name__ == '__main__':
    main()