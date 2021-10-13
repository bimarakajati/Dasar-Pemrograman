print('Masukkan 10 data bil bulat:')
data = []
for i in range(1,11):
    data.append(int(input(f'bil {i} = ')))
print(f'rata-rata = {sum(data)/len(data)}')
print('daftar nilai diatas rata-rata')
for i in data:
    if i >= sum(data)/len(data):
        print(i)