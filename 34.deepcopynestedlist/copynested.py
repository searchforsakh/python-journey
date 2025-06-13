## COPY NESTED 

data0 = [1,2]
data1 = [3,4]

data_gabung = [data0, data1, 100]
data_gabung_copy = data_gabung.copy()

print(f"data gabung = {data_gabung}")
print(f"data gabung copy = {data_gabung_copy}")

# address dari data gabung
print(f"address data gabung\t\t= {hex(id(data_gabung))}")
print(f"address data gabung copy\t= {hex(id(data_gabung_copy))}")

print("\naddress dari member ke 1")
print(f"address member 1 data gabung\t\t= {hex(id(data_gabung[0]))}")
print(f"address member 1 data gabung copy\t= {hex(id(data_gabung_copy[0]))}")


# mengambil data untuk nested list
data = data_gabung[0][1] # [untuk menentukan list][untuk mengambil data didalam list]
print(f"data = {data}")

data_gabung[0][1] = 456
data_gabung[2] = 200
print(f"data gabung = {data_gabung}")
print(f"data gabung copy = {data_gabung_copy}")

# gunakan deepcopy jika ingin mengcopy nested list
from copy import deepcopy

data_gabung = [data0, data1, 100]
data_gabung_deepcopy = deepcopy(data_gabung)

print(f"address data gabung\t\t= {hex(id(data_gabung))}")
print(f"address data gabung deepcopy\t= {hex(id(data_gabung_deepcopy))}")

print("\naddress dari member ke 1")
print(f"address member 1 data gabung\t\t= {hex(id(data_gabung[0]))}")
print(f"address member 1 data gabung deepcopy\t= {hex(id(data_gabung_deepcopy[0]))}")

data_gabung[0][1] = 40
print(f"data gabung = {data_gabung}")
print(f"data gabung copy = {data_gabung_copy}")
print(f"data gabung deepcopy = {data_gabung_deepcopy}")
