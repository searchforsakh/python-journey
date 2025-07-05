# TEMPLATE FUNGSI DENGAN RETURN
# def nama_fungsi(input/argumen)
    # badan fungsi
    # return output

# MEMBUAT FUNGSI KUADRAT
def kuadrat(angka):
    return angka**2
y = kuadrat(3)
print(y)
print(kuadrat(10))
z = kuadrat(5) + 5
print(z)

# MEMBUAT FUNGSI TAMBAH (dengan multi return)
def tambah(angka1, angka2):
    return angka1 + angka2
print(tambah(1,2))
y = tambah(5,8)
print(y)
a = tambah(2,7) + 10
print(a)

# MEMBUAT FUNGSI DENGAN RETURN BANYAK
print()
def operasi_hitung(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi

a,b,c,d = operasi_hitung(5,5) #harus sesuai dengan urutan return
print(f"hasil tambah {a}")
print(f"hasil kurang {b}")
print(f"hasil kali {c}")
print(f"hasil bagi {d}")
