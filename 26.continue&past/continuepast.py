# continue, pass, break
# pass --> berfungsi sebagai dummy, tidak akan dieksekusi

# PASS
"""
angka = 0
while angka < 5:
    angka += 1

    if angka == 3:
        pass # --> ini tidak akan dieksekusi

    print(angka)
"""

# CONTINUE
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("HAI") # aksi continue
        continue # semua looping yang ada dibawah akan diskip, loncat ke step selanjutnya

    print("HALO") # aksi 2
print("thanku")