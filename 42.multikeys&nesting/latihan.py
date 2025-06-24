import datetime

mahasiswa1 = {
    'nama' : 'Sakha Pratama',
    'tgllahir' : datetime.date(2006,11,6),
    'jurusan' : 'Informatika',
    'jumlahsks' : '50',
    'beasiswa' : True
}
mahasiswa3 = {
    'nama' : 'Jova Nurfadhil',
    'tgllahir' : datetime.date(2006,5,2),
    'jurusan' : 'DKV',
    'jumlahsks' : '20',
    'beasiswa' : False
}
mahasiswa2 = {
    'nama' : 'Alfaes',
    'tgllahir' : datetime.date(2004,9,30),
    'jurusan' : 'Farmasi',
    'jumlahsks' : '30',
    'beasiswa' : True
}

nim_mahasiswa = {
    '0062957117' : mahasiswa1,
    '0062956597' : mahasiswa2,
    '0062951234' : mahasiswa3
}

print(f"{'NIM':^13} {'NAMA':^17} {'Jurusan':^15} {'SKS':^5} {'BEASISWA':^5}")

for data in nim_mahasiswa:
    nama = nim_mahasiswa
    print(nama)

# print("\nMasukkan Data Mahasiswa")
# inputusernama = input("Masukkan nama mahasiswa : ")
# inputuserjurusan = input("Masukkan Jurusan : ")
# inputusersks = input("Masukkan Jumlah SKS : ")

# data_mahasiswa = {
#     'nama' : inputusernama,
#     'jurusan' : inputuserjurusan,
#     'sks' : inputusersks
# }

# list_kosong = {}
# while True:
#     list_kosong.append(data_mahasiswa)
#     data_mahasiswa = {
#         'nama' : inputusernama,
#         'jurusan' : inputuserjurusan,
#         'sks' : inputusersks
#     }
#     print(data_mahasiswa)

