## LOOPING LIST

# MENGGUNAKAN FOR LOOP --> cara simpel
print("Menggunakan for loop")
kumpulan_angka = [1,4,5,8,2,5,3,7]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Freya", "Michie", "Shani", "Marsha", "Kathrina"]
for nama in peserta:
    print(f"nama peserta = {nama}")

# MENGGUNAKAN FOR LOOP DAN RANGE --> cara ribet
print("Menggunakan for loop dan range")
kumpulan_angka = [1,4,5,8,2,5,3,7]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# MENGGUNAKAN WHILE LOOP
print("Menggunakan while loop")
kumpulan_angka = [1,4,5,8,2,5,3,7]
panjang = len(kumpulan_angka)

i = 0
while True:
    if i < panjang:
        print(f"angka = {kumpulan_angka[i]}")
        i += 1
    else:
        break

# MENGGUNAKAN LIST COMPREHENSION
print("Menggunakan list comprehension")

data = [1,4,5,8,"sakha",5,3,7]
[print(f"data = {i}") for i in data]

kumpulan_angka = [1,4,5,8,2,5,3,7]
angka_kuadrat = [i**2 for i in kumpulan_angka]
print(angka_kuadrat)

# MENGGUNAKAN ENUMERATE --> UNTUK MENDAPATKAN INDEX DAN DATANYA SEKALIGUS
print("Menggunakan enumerate")
empty_list = []
data10 = "river"
data20 = "fiersa"
data = [data10, data20]
empty_list.append(data) # --> list kosong akan ditambah dari setiap data yang dimasukkan
for index, data in enumerate(empty_list):
    print(f"index = {index} data = {data[0]} data2 = {data[1]} data1 = {data[0]}")


