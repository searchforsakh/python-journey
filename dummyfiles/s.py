# # # Contoh penggunaan if else
# # nilai = float(input("Masukkan nilai anda = "))

# # if nilai >= 80:
# #     print("Anda mendapatkan nilai A.")
# # else:
# #     print("Anda mendapatkan nilai di bawah A.")

# # Contoh penggunaan if elif else
# nilai = float(input("Masukkan nilai anda = "))

# if nilai >= 90:
#     print("Anda mendapatkan nilai A.")
# elif nilai >= 80:
#     print("Anda mendapatkan nilai B.")
# elif nilai >= 70:
#     print("Anda mendapatkan nilai C.")
# else:
#     print("Anda mendapatkan nilai di bawah C.")
print("\nprogram hitung rumus bangun datar")
    
print("""1. segitiga
2. persegi
3. persegi panjang
4. trapesium""")

pilihrumus = int(input("pilih salah satu bangun datar = "))
if  pilihrumus == 1:
    print("\nmenghitung rumus luas dan keliling segitiga")
alas = float(input("masukkan alas segitiga = "))
tinggi = float(input("masukkan tinggi segitiga = "))
luas = 1/2 * alas * tinggi
print(f'rumus luas segitiga = {luas}')
pythagoras = (alas**2) + (tinggi**2)
keliling = (pythagoras**0.5) + alas + tinggi
print(f'rumus keliling segitiga = {keliling}')
lanjutornot = input("ingin lanjut mencari rumus? Y/N = ")

if lanjutornot == "Y":
    print("""1. segitiga
2. persegi
3. persegi panjang
4. trapesium""")

pilihrumus = int(input("pilih salah satu bangun datar = "))





print("\nmenghitung rumus luas dan keliling persegi")
sisi = float(input("masukkan sisi persegi = "))
luas = sisi * sisi
keliling = 4 * sisi
print(f"rumus luas persegi adalah = {luas}")
print(f"rumus keliling persegi adalah = {keliling}")

