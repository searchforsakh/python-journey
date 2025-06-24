import datetime
import string
import random
import os
os.system('cls')


# template dict
mahasiswa_template = {
    'nama' : '',
    'jurusan' : '',
    'nim' : '',
    'sks_lulus' : '',
    'tgl_lahir' : datetime.date(1111,1,1)
}


data_mahasiswa = {}
while True:
    print(f"{"DATABASE MAHASISWA":^30}")
    print(f"{"ESA UNGGUL":^30}")
    print("~"*30)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys()) #membuat dictinary baru dengan key dari template dan value none
    mahasiswa['nama'] = input('Masukkan Nama Mahasiswa = ')
    mahasiswa['jurusan'] = input('Jurusan = ')
    mahasiswa['nim'] = int(input('NIM = '))
    mahasiswa['sks_lulus'] = int(input('SKS LULUS = '))
    tahun = int(input("Tahun Lahir = "))
    bulan = int(input("Bulan Lahir = "))
    tanggal = int(input("Tanggal Lahir = "))
    mahasiswa['tgl_lahir'] = datetime.datetime(tahun,bulan,tanggal)

    key = ''.join(random.choice(string.ascii_letters) for i in range(5))
    data_mahasiswa.update({key : mahasiswa})

    print(f"{'Key':<7} {'Nama Mahasiswa':<20} {'Jurusan':<20} {'NIM':<10} {'SKS LULUS':<10} {'Tanggal Lahir':<10}")
    print("-"*85)
    
    for i in data_mahasiswa:
        nama = data_mahasiswa[i]['nama']
        jurusan = data_mahasiswa[i]['jurusan']
        nim = data_mahasiswa[i]['nim']
        sks = data_mahasiswa[i]['sks_lulus']
        tgllahir = data_mahasiswa[i]['tgl_lahir'].strftime("%x")
        print(f"{i:<7} {nama:<20} {jurusan:<20} {nim:<10} {sks:<10} {tgllahir:<10}")
   
    confirm_usr = input('mau lanjut ? = (y/n) ')
    if confirm_usr == 'n':
        break
