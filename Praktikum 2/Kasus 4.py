#kamus
a = 1
b = 4
#algoritma
print('hasil a yang pertama:', a)
print('hasil b yang pertama: '+str(b))
b = a - -1
a -= b #ini ekuivalen dengan a = a - b
print('hasil a yang kedua: '+str(a))
print('hasil b yang kedua:', b)
a = b + 2
b = a * b
print('hasil a yang ketiga: {}'.format(a))
print('hasil b yang ketiga: %f' %(b))
#berikut adalah cara menukar nilai pada dua variabel dengan assignment
c = a
a = b
b = c
print('hasil a yang keempat: {}'.format(a))
print('hasil b yang keempat: {}'.format(b))