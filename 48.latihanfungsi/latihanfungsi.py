# # #header
# # import os
# # os.system("cls")
# # print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# # print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# # print(f"{"#"*40:^40}\n")

# # # mengambil input user
# # panjang = int(input("Masukkan Nilai Panjang = "))
# # lebar = int(input("Masukkan Nilai lebar = "))

# # # program menghitung luas dan keliling
# # luas = panjang*lebar
# # keliling = 2*(panjang+lebar)

# # # menampilkan hasilnya
# # print("Hasil luas, ",luas)
# # print("Hasil keliling, ",keliling)

# def header():
#     import os
#     os.system("cls")
#     print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
#     print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
#     print(f"{"#"*40:^40}\n")

# def inputuser():
#     panjang = int(input("Masukkan Nilai Panjang = "))
#     lebar = int(input("Masukkan Nilai lebar = "))
#     return panjang, lebar

# def hitungluas(panjang,lebar):
#     luas = panjang*lebar
#     return luas

# def hitungkeliling(panjang,lebar):
#     keliling = 2*(panjang+lebar)
#     return keliling

# def hasil(message,value):
#     print(f"Hasil dari {message} adalah = {value}")

# while True:
#     header()

#     opsi = int(input("Masukkan pilihan anda \n1. Menghitung Luas\n2. Menghitung Keliling\n3. Keluar Program = "))
#     if opsi == 1:
#         panjang, lebar = inputuser()
#         luas = hitungluas(panjang, lebar)
#         hasil("Luas", luas)

#     elif opsi == 2:
#         panjang, lebar = inputuser()
#         keliling = hitungkeliling(panjang, lebar)
#         hasil("keliling", keliling)
#     else:
#         break

#     iscontinue = input("apakah ingin lanjut? (y/n) = ")
#     if iscontinue == "n":
#         break
# print("PROGRAM SELESAI, Terimakasih.")

# header

def header():
    import os
    os.system('cls')
    print(f"{"PROGRAM MENGHITUNG RUMUS PERSEGI PANJANG":^60}")
    print(f"{"-"*60:^60}")

def inputuser():
    panjang = int(input("Masukkan panjang = "))
    lebar = int(input("Masukkan lebar = "))
    return panjang,lebar

def hitungluas(panjang,lebar):
    luas = panjang*lebar
    return luas

def hitungkeliling(panjang,lebar):
    keliling = 2*(panjang+lebar)
    return keliling

def display(message, value):
    print(f"hasil dari {message} adalah {value}")

def options1():
    panjang,lebar = inputuser()
    luas = hitungluas(panjang,lebar)
    display("luas", luas)

def options2():
    panjang,lebar = inputuser()
    keliling = hitungkeliling(panjang,lebar)
    display("keliling", keliling)

def options3():
    panjang,lebar = inputuser()
    luas = hitungluas(panjang,lebar)
    keliling = hitungkeliling(panjang,lebar)
    display("luas", luas)
    display("keliling", keliling)

while True:
    header()

    opsi = int(input("""
Masukkan Pilihan Anda
1. Hitung Luas
2. Hitung Keliling
3. Hitung Keduanya
4. Keluar Program
= """))
    
    if opsi == 1:
        options1()
    elif opsi == 2:
        options2()
    elif opsi == 3:
        options3()
    elif opsi == 4:
        print("Program Selesai, Terimakasih.")
        break
    else:
        break
    
    iscontinue = input("Apakah Ingin Lanjut? (y/n) = ")
    if iscontinue == "n":
        break