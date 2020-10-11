# Uang anak kos

# kamus
kos = 500000 # biaya kos
makan = 500000 # uang buat makan/jajan
buku = 200000 #uang buat beli buku

pengeluaran = kos + makan + buku 
sangu = int(input('Uang bulanan yang diberikan ortu Soni: '))

tiket_biasa = 500000
tiket_vip = 1000000

#algoritma
if sangu >= pengeluaran:
    uang = sangu - pengeluaran
    if uang >= tiket_vip:
        print('Soni jadi menonton konser dengan tempat duduk VIP')
    elif tiket_biasa <= uang < tiket_vip:
        print('Soni jadi menonton konser dengan tempat duduk biasa')
    else:
        print('Soni tidak bisa menonton konser karena uang kurang')
else:
    print('Input tidak valid')