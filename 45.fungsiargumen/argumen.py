'''fungsi dengan argumen (input)'''

# TEMPLATE FUNGSI DENGAN ARGUMEN
# def nama_fungsi(input/argumen)
    # badan fungsi

# FUNGSI DENGAN STRING
def welcome(nama):
# fungsi welcome mendapat input dengan variabel nama
    print(f"Selamat datang! {nama}.")
welcome("Sakha")
welcome("Sakhi")

# FUNGSI DENGAN INTEGER
def calc(angka1,angka2):
    hasil = angka1 * angka2
    print(f"hasil {angka1} * {angka2} = {hasil}")
calc(7,7)

# FUNGSI DENGAN LIST
def absen(list_peserta):
    peserta = list_peserta.copy()
    list_peserta[2] = "sakha"
    for data in peserta:
        print(f"Halo selamat datang bapak {data}")

daftar_murid = ["Sakha", "Budi", "Marsel", "AZKA", 1, False]
absen(daftar_murid)
print(daftar_murid)