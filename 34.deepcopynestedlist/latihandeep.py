## GUNAKAN DEEPCOPY JIKA INGIN MENGCOPY NESTED LIST (GUNAKAN VARIABLE PENAMPUNG)

from copy import deepcopy
data1 = [5,6]
data2 = [7,8]

data_gabung = [data1, data2]
print(f'data gabung = {data_gabung}')
print(f'address data gabung = {hex(id(data_gabung))}')

data_copy = deepcopy(data_gabung)
print(f'data gabung = {data_copy}')
print(f'address data copy = {hex(id(data_copy))}')

data_gabung[0][1] = 300
print(f'data gabung = {data_gabung}')
print(f'data copy = {data_copy}')
