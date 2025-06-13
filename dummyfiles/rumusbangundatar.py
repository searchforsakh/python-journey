def hitungsegitiga():
    print("\nPROGRAM WAS READY")
    alas = float(input("masukkan alas segitiga = "))
    tinggi = float(input("masukkan tinggi segitiga = "))
    luas = 1/2 * alas * tinggi
    print(f'luas segitiga = {luas}')
    pythagoras = (alas**2) + (tinggi**2)
    keliling = (pythagoras**0.5) + alas + tinggi
    print(f'keliling segitiga = {keliling}')

def hitungpersegi():
    print("\nPROGRAM WAS READY")
    sisi = float(input("masukkan sisi persegi = "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print(f"luas persegi adalah = {luas}")
    print(f"keliling persegi adalah = {keliling}")

def hitungpersegipanjang():
    print("\nPROGRAM WAS READY")
    panjang = float(input("Masukkan panjang = "))
    lebar = float(input("Masukkan lebar = "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas persegi panjang = {luas}")
    print(f"keliling persegi panjang = {keliling}")
    
def hitungtrapesium():
    print("\nPROGRAM WAS READY")
    sisiatas = float(input("Masukkan sisi atas = "))
    sisibawah = float(input("Masukkan sisi bawah = "))
    tinggi = float(input("Masukkan tinggi = "))
    bawahphytagoras = (sisibawah - sisiatas) / 2
    phytaghoras = ((bawahphytagoras**2) + (tinggi**2))**0.5
    keliling = (phytaghoras*2) + sisiatas + sisibawah
    luas = 1/2 * (sisiatas + sisibawah) * tinggi
    print(f"Luas trapesium adalah = {luas}")
    print(f"keliling trapesium adalah = {keliling}")

while True:
    inputuser = int(input("""
    PROGRAM HITUNG LUAS DAN KELILING BANGUN RUANG\n
    0. END PROGRAM
    1. SEGITIGA
    2. PERSEGI
    3. PERSEGI PANJANG
    4. TRAPESIUM\n
    PILIH ANGKA YANG INGIN DIHITUNG = """))
    if inputuser == 1:
        hitungsegitiga()
    elif inputuser == 2:
        hitungpersegi()
    elif inputuser == 3:
        hitungpersegipanjang()
    elif inputuser == 4:
        hitungtrapesium()
    else:
        break

## WAJIB GUNAKAN IF ELIF ELSE JIKA MEMILIKI KONDISI TRUE LEBIH DARI SATU