#input
pjg = int(input('Panjang tanah: '))
lbr = int(input('Lebar tanah: '))
x = input('Apakah Pak Joni dan Pak Soni setuju? ')
#output
if 'setuju' in x :
    print(float(pjg * lbr), '\n', float((pjg * lbr) / 2))
else :
    print(float(pjg * lbr), '\n', float(pjg * lbr))