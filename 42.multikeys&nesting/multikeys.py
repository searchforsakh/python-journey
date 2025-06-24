# #program database warung
import datetime

# makanan1 = {
#     'nama barang' : 'chiki',
#     'nama merk' : 'zeky',
#     'jumlah barang' : '1000',
#     'tanggal basi' : datetime.datetime(2025,1,10)
# }
# makanan2 = {
#     'nama barang' : 'biskuit',
#     'nama merk' : 'oreo',
#     'jumlah barang' : '99',
#     'tanggal basi' : datetime.datetime(2025,1,10)
# }
# makanan3 = {
#     'nama barang' : 'cokelat',
#     'nama merk' : 'silverqueen',
#     'jumlah barang' : '1000',
#     'tanggal basi' : datetime.datetime(2025,1,10)
# }

# data_makanan = {
#     "MKN001" : makanan1,
#     "MKN002" : makanan2,
#     "MKN003" : makanan3
# }

# print(f"{'KB':<6} {'BARANG':<15} {'MERK':<13} {'STOK':<7} {'EXP':<10}")

# for i in data_makanan:
#     barang = data_makanan[i]['nama barang']
#     merk = data_makanan[i]['nama merk']
#     stok = data_makanan[i]['jumlah barang']
#     exp = data_makanan[i]['tanggal basi'].strftime("%x")
#     print(f"{i:<6} {barang:<15} {merk:<13} {stok:<7} {exp:<10}")

#     # print(i)
#     # print(merk)
#     # print(stok)
#     # print(exp)

makanan4 = {
    'nama barang' : 'chiki',
    'nama merk' : 'zeky',
    'jumlah barang' : '1000',
    'tanggal basi' : datetime.datetime(2025,1,10)
}

print(f"{'BARANG':<15} {'MERK':<13} {'STOK':<7}")

for i in makanan4:
    value = i
    print(i)

for i in makanan4.keys():
    print(i)
    # print(f"{i['nama barang']:<15} {i['nama merk']:<13} {i['jumlah barang']:<7}")