pjg = int(input('panjang: '))
lbr = int(input('lebar: '))

for i in range(pjg):
   print('*', end='')
print('\t')
for j in range(lbr-2):
   print('*', ' '*(pjg-4), '*')
for i in range(pjg):
   print('*', end='')