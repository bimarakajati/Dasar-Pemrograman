nm = str(input("Masukkan Nama: "))
ipk = float(input("Masukkan IPK : "))
akredit = str(input("Akreditasi Universitas :")).casefold
if ipk >= 3.0 :
        akademik = int(input("Nilai Akademik :"))
        ketrampilan = int(input("Nilai Keterampilan :"))
        psikologi = int(input("Nilai psikologikologi :"))
        ratarata = (akademik + ketrampilan + psikologi) / 3
else :
        print("Mohon Maaf Saudara {} Anda Kami Tolak".format(nm))
if ratarata >= 80 :
    print("Nilai Rata :",ratarata)
    if akademik > ketrampilan > psikologi :
        print("Selamat {} anda diterima,dan ditempatkan di bagian Manajemen".format(nm))
    elif akademik > psikologi > ketrampilan :
        print("Selamat {} anda diterima,dan ditempatkan di bagian Manajemen".format(nm))
    elif ketrampilan > psikologi > akademik : 
        print("Selamat {} anda diterima,dan ditempatkan di bagian Produksi".format(nm))
    elif ketrampilan > akademik > psikologi:
        print("Selamat {} anda diterima,dan ditempatkan di bagian Produksi".format(nm))
    elif psikologi > akademik > ketrampilan:
        print("Selamat {} anda diterima,dan ditempatkan di bagian Pemasaran".format(nm))
    elif psikologi > ketrampilan > akademik:
        print("Selamat {} anda diterima,dan ditempatkan di bagian Pemasaran".format(nm))
else :
    print("Mohon Maaf Saudara {} Tidak Lulus Karena Ada Nilai Dibawah 80".format(nm))