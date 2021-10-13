#kamus
import getpass

username = input('Masukkan username: ')
password = input('Masukkan password: ')
print('Akun berhasil dibuat')

#algoritma
n = 0
while n < 3:
    print('\nSilahkan masukkan user dan password anda kembali')
    username_input = input('username = ')
    password_input = getpass.getpass('password = ')
    if username == username_input:
        if password == password_input:
            print('\nLogin sukses. Selamat datang {}!!!\n' .format(username))
            break
        else:
            print('Password salah!')
            n+=1
    else:
        print('Akun tidak terdaftar')
        n+=1
else:
    print('\nMaaf, anda memasukkan username dan password yang salah selama 3x, program berhenti')