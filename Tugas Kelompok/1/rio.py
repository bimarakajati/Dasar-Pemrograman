def alasan():
    jurusan = input("Apa jurusan anda ? ")
    alasan = input("Mengapa anda memilih jurusan tersebut ? ")
    belajar = input("Siap untuk mengikuti pembelajaran ? ")
    print("------------------------")
    print("Jurusan anda " + jurusan)
    print("Alasan anda memilih jurusan karena " + alasan)
    print("Anda " + belajar, "untuk mengikuti pembelajaran")
    
def salam():
    nama = input("Siapa nama anda ? ")
    umur = input("Berapa umur anda ? ")
    kabar = input("Bagaimana kabar anda ? ")
    print("------------------------")
    print("Nama anda : " + nama)
    print("Umur anda : " + umur)
    print("Kabar anda : " + kabar)

def menu():
    print ("\n")
    print("-----MENU-----")
    print ("[1] Perkuliahan")
    print ("[2] Biodata")
    print ("[3] Keluar")
    pdog = input("Pilih sesuai angka untuk melanjutkan > ")
    if(pdog == "1"):
        alasan()
        kembali()
    elif(pdog == "2"):
        salam()
        kembali()
    elif(pdog == "3"):
        exit()
    else:
        print ("\n")
        print("Error : input angka salah !")

def kembali():
    print ("\n")
    print ("Tekan 'y' untuk melanjutkan, dan 'n' untuk keluar !")
    lagi = input("Mau kembali lagi ? ")
    if(lagi == "y"):
        menu()
    elif(lagi == "n"):
        print ("\n Terima kasih telah menggunakan :)")
        exit()
    else:
        print("Thank you :)")
        exit()

def login():
    print ("Buat user dan password terlebih dahulu : \n")
    user = input("Masukkan Username: ")
    pas = input("Masukkan Password: ")
    print ("\n Silahkan login : \n")
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")
    if username == user:
        if password == pas:
            print ("\n Selamat datang",username, "!")
            menu()
        else :
            print ("Password salah!")
    else :
        print ("Akun tidak terdaftar !")

login()