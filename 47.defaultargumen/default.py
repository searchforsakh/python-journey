# contoh default argumen

# TEMPLATE FUNGSI DENGAN DEFAULT ARGUMEN
# def nama_fungsi(input/argumen = "nilai default")
    # badan fungsi

# contoh 1
def namasiswa(nama = "ABSEN"): # ABSEN adalah nilai default yg diberikan
    print(f"Halo Selamat datang {nama}")
namasiswa("Sakha")
namasiswa() # Jika tidak ada input, maka akan menampilkan nilai default
print()

#contoh 2
def absensi(nama, pesan = "welcome"): #welcome adalah nilai default yg akan ditampilkan jika tidak ada input yg dimasukkan
    print(f"{pesan}, bapak/ibu {nama}")

absensi("sakha","selamat datang") # posisi harus sesuai dengan argumen/inputnya 
absensi("sakhi")
absensi("sakhuy", pesan = "halo")

# contoh 3
def pangkat(angka1,pangkat=2): # akan memberikan nilai default pangkat2
    hasil = angka1**pangkat
    return hasil
print(pangkat(2,2))
print(pangkat(5))
print(pangkat(3,pangkat = 3))

y = pangkat(pangkat=5, angka1=2)
print(y)

# contoh 4
def fungsi(input1=1, input2=2, input3=3, input4=4):
    return input1 + input2 + input3 + input4
print(fungsi(input1=3))