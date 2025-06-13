# BREAK
data_int = int(input("Hitung sampai = "))
angka = 99

while True:
    angka += 1
    print(f"count --> {angka}") # aksi 1

    if angka == data_int:
        print("ANGKA TERAKHIR") # aksi break
        break # jika sudah menemukan break maka looping akan selesai.
    
    print("HALOO") # aksi 2
print("END PROGRAM")