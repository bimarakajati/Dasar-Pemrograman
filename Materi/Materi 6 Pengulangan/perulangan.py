#berdasarkan jumlah pengulangan

""" # For loop
for i in range(10):
    print('hello')

# While loop
n = 10
while n:
    print("hello")
    n-=1 """

#berdasarkan kondisi berhenti

""" #while
n = 1
while True:
    print('hello')
    n+=1
    if n > 10:
        break

#for 
for n in range(999):
    print('hello')
    if n > 8:
        break """

#berdasarkan kondisi perulangan
""" n = 0
while n >= 0 and n < 10:
    n+=1
    print('hello') """

#berdasarkan dua ekspresi

""" #while
n = 1
while True:
    print('hello')
    n+=1
    if n > 10:
        print('stop')
        break

#for
for i in range(999):
    print('hello')
    if i > 8:
        break """

#berdasarkan pencacah

""" #for 1
for i in range(0,10):
    print('hello')

#for 2
for i in range(0,20,2):
    print('hello') """

#break statement
n = 1
batas = int(input())
while n <= batas:
    if n > 5:
        break
    print(n)
    n+=1
print('selesai')

#continue statement
""" n = 0
batas = int(input())
while n < batas:
    n+=1
    if n == 5:
        continue
    print(n)
print('selasai') """