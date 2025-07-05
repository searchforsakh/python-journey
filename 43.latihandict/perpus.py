# PROGRAM DATABASE PERPUS
import random
import string
import os
os.system('cls')

inputuser = {
    'judul' : '',
    'penulis' : '',
    'penerbit' : '',
    'tahun terbit' : ''
}

data_user = {}
while True:
    print(f"{"WELCOME TO DATABASE":^30}")
    print(f"{"UEU LIBRARY":^30}")

    data_buku = dict.fromkeys(inputuser.keys())
    data_buku['judul'] = input("Masukkan Judul Buku = ")
    data_buku['penerbit'] = input("Penerbit = ")
    data_buku['penulis'] = input("Penulis = ")
    data_buku['tahun terbit'] = int(input("Tahun Terbit (YYYY) = "))

    keys = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_user.update({keys : data_buku}) # Nilai paling tinggi dalam dict, setiap data buku yang ditambahkan, akan diberi keys dari variable random keys diatas(no.26)
    print(f"{"KEY":<8} {"JUDUL BUKU":<20} {"PENERBIT BUKU":<20} {"PENULIS BUKU":<20} {"TAHUN TERBIT":<10}")
    print("~"*78)
    
    for key in data_user:
        judulbuku = data_user[key]['judul']
        penerbitbuku = data_user[key]['penerbit']
        penulisbuku = data_user[key]['penulis']
        tahunterbit = data_user[key]['tahun terbit']
        print(f"{key:<8} {judulbuku:<20} {penerbitbuku:<20} {penulisbuku:<20} {tahunterbit:<10}")

    conf_usr = input("LANJUT MENGINPUT ? (y/n) = ")
    if conf_usr == 'n':
        break
