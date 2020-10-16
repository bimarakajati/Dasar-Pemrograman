#Kasus If Else If Test Kepribadian
print("Jawab: Sendiri/Beramai")
Sdr = "Sendiri"
Brm = "Beramai"
Test_1 = str(input("Anda Lebih Senang Sendiri/Beramai Saat Ingin Memulihkan Energy: "))
print("Jawab: Ya/Tidak")
plh_1 = "Ya"
plh_2 = "Tidak"
Test_2 = str(input("Anda Senang Jika Ada Acara Mendadak? "))
print("Jawab:Nongkrong/Merenung")
sifat_1 = "Nongkrong"
sifat_2 = "Merenung"
Test_3 = str(input("Lebih Suka Nongkrong Atau Memikirkan Sesuatu? "))
if (Test_1 == Sdr and Test_2 == plh_2 and Test_3 == sifat_2) :
    print("Kepribadian Anda Introvert")
elif (Test_1 == Sdr and Test_2 == plh_1 and Test_3 == sifat_2) :
    print("Kepribadian Anda Introvert Khusus")
elif (Test_1 == Brm and Test_2 == plh_1 and Test_3 == sifat_1) :
    print("Kepribadian Anda Extrovert")
elif (Test_1 == Brm and Test_2 == plh_2 and Test_3 == sifat_1) :
    print("Kepribadian Anda Ekstrovert Khusus")
else :
    print("Mungkin Anda Ambivert")