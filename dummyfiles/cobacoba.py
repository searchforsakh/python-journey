# ## SISTEM PERHITUNGAN KASIR SEDERHANA.
# print("\n",10*"-"+"Masukkan barang yang dibeli"+10*"-")

# s = 8000
# d = 9000
# p = 7000

# sayap = int(input("masukkan jumlah membeli sayap\t = "))
# dada = int(input("masukkan jumlah membeli dada\t = "))
# paha = int(input("masukkan jumlah membeli paha\t = "))

# print("\n","-"*10+"Jumlah harga yang harus dibayar"+10*"-")
# jumlah_jenis = (f"""Jumlah harga sayap = {sayap*s:,}
# Jumlah harga dada  = {dada*d:,}
# Jumlah harga paha  = {paha*p:,}""")
# print(jumlah_jenis)

# print("\n","-"*10+"Total Harga"+10*"-")
# total = ((sayap*s) + (dada*d) + (paha*p))
# print(f"Total = {total:,}")

# #membuat segitiga keatas
# count = 1
# sisi = 10
# spasi = int(sisi/2)
# while True:
#     if count%2:
#         print(" "*spasi, "%"*count)
#         count += 1
#     else:
#         spasi -= 1
#         count += 1
#     if sisi < count:
#         break

# # membuat segitiga kebawah
# count = 10
# sisi = 1
# spasi = int(count%2)
# while True:
#     if count%2:
#         print(" "*spasi, "%"*count,)
#         count -= 1
#     else:
#         spasi += 1
#         count -= 1
#     if sisi > count:
#         break

# data = range(10,20)
# for i in data: 
#     print(data)
# print("END FOR")

#membuat trapesium
#membuat kotak
# count = 5
# count2 = 1
# count3 = 1
# spasi = int(15/2)
# for i in range(8):
#         print(" "*spasi + "#"*count3 + "#"*count + "#"*count2)
#         spasi -= 1
#         count2 += 1
#         count3 += 1

kumpulan_angka = [1,2,5,6,7,3,2,4,5]
for angka in kumpulan_angka:
    print(f"angka = {angka}")