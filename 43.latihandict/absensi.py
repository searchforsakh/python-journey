# PROGRAM ABSENSI SEDERHANA
import os
import random
import string
os.system("cls")

print(f"{"SELAMAT DATANG":^50}")
print(f"{"SILAHKAN MASUKKAN ABSENSI":^50}")


template = {
    "nama" : "",
    "jabatan" : "",
    "jam masuk" : ""
}

data_user = {}
while True:
    inputdata = dict.fromkeys(template) # membuat variabel baru yang nantinya akan diisi oleh user
    inputdata["nama"] = input("\nmasukkan nama anda\t = ")
    inputdata["jabatan"] = input("""masukkan jabatan anda\t 
1. Karyawan
2. OB
3. Satpam\t\t = """)
    while inputdata["jabatan"] <= "3":
        if inputdata["jabatan"] == "1":
            inputdata["jabatan"] = "Karyawan"
        elif inputdata["jabatan"] == "2":
            inputdata["jabatan"] = "OB"
        elif inputdata["jabatan"] == "3":
            inputdata["jabatan"] = "Satpam"
        else:
            print("Tolong Masukkan Jabatan yang Sesuai\n")
            inputdata["jabatan"] = input("""masukkan jabatan anda\t 
1. Karyawan
2. OB
3. Satpam\t\t = """)
    
    inputdata["jam masuk"] = int(input("masukkan jam masuk anda\t = "))
    
    keys = "".join(random.choice(string.digits)for i in range(4))
    data_user.update({keys : inputdata})

    print(f"\n{"code":<7} {"Nama":<20} {"Jabatan":<20} {"Jam Masuk":<10}")
    print("="*70)

    for key in data_user:
        nama = data_user[key]["nama"]
        jabatan = data_user[key]["jabatan"]
        jammasuk = data_user[key]["jam masuk"]
        if jammasuk > 9:
            print(f"{key:<7} {nama:<20} {jabatan:<20} {jammasuk:<10} *telat")
            continue
        print(f"{key:<7} {nama:<20} {jabatan:<20} {jammasuk:<10}")
    quit_answer = input("\nlanjut menginput? (y/n) = ")
    if quit_answer == "n":
        break

