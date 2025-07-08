# #header
# import os
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{"#"*40:^40}\n")

# # mengambil input user
# panjang = int(input("Masukkan Nilai Panjang = "))
# lebar = int(input("Masukkan Nilai lebar = "))

# # program menghitung luas dan keliling
# luas = panjang*lebar
# keliling = 2*(panjang+lebar)

# # menampilkan hasilnya
# print("Hasil luas, ",luas)
# print("Hasil keliling, ",keliling)

def header():
    import os
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{"#"*40:^40}\n")

def inputuser():
    panjang = int(input("Masukkan Nilai Panjang = "))
    lebar = int(input("Masukkan Nilai lebar = "))
    return panjang, lebar

def hitungluas(panjang,lebar):
    luas = panjang*lebar
    return luas

def hitungkeliling(panjang,lebar):
    keliling = 2*(panjang+lebar)
    return keliling

def hasil(message,value):
    print(f"Hasil dari {message} adalah = {value}")

while True:
    header()
    
    opsi = int(input("Masukkan pilihan anda \n1. Menghitung Luas\n2. Menghitung Keliling\n3. Keluar Program = "))
    if opsi == 1:
        panjang, lebar = inputuser()
        luas = hitungluas(panjang, lebar)
        hasil("Luas", luas)

    elif opsi == 2:
        panjang, lebar = inputuser()
        keliling = hitungkeliling(panjang, lebar)
        hasil("keliling", keliling)
    else:
        break

    iscontinue = input("apakah ingin lanjut? (y/n) = ")
    if iscontinue == "n":
        break
print("PROGRAM SELESAI, Terimakasih.")

