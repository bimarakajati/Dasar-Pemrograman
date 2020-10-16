# Program kalkulator sederhana

# Kamus
jawab = 'ya' # Agar program bisa ke menu setelah selesai melakukan operasi

while jawab == 'ya':
    print('\nSelamat datang di Program Kalkulator Sederhana\n')

    # Menu kalkulator
    print('Menu operasi')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Sisa Pembagian')
    
    # Input dari user
    pilihan = input('\nMasukkan pilihan(1-5): ')
    
    bil1 = int(input('\nMasukkan bilangan pertama: '))
    bil2 = int(input('Masukkan bilangan kedua: '))

    if pilihan == '1': # Penjumlahan
        penjumlahan = bil1 + bil2
        print(bil1,'+',bil2,'=', penjumlahan)
    elif pilihan == '2': # Pengurangan
        pengurangan = bil1 - bil2
        print(bil1,'-',bil2,'=', pengurangan)
    elif pilihan == '3': # Perkalian
        perkalian = bil1 * bil2
        print(bil1,'x',bil2,'=', perkalian)
    elif pilihan == '4': # Pembagian
        pembagian = bil1 / bil2
        print(bil1,':',bil2,'=', pembagian)
    elif pilihan == '5': # Modulus
        modulus = bil1 % bil2
        print(bil1,'%',bil2,'=', modulus)
    else: # Input salah apabila user memasukkan selain angka 1-5
        print('Input salah')

    jawab = input('\nIngin kembali ke menu (ya/tidak)? ')