## program kalkulator sederhana

print("\n"+"="*5+"Program Kalkulator Sederhana"+"="*5)

angka_1 = float(input("\nMasukkan Angka Pertama\t\t= "))
operator = input("Masukkan operator (+, -, *, /)\t= ") #KONDISI UTAMA #start/mulai
angka_2 = float(input("Masukkan Angka Kedua\t\t= "))

if operator == "+": ##KONDISI PERTAMA (TRUE)
    hasil = angka_1 + angka_2 
    print(f"\nHasilnya adalah {hasil}")
elif operator == "-": ##KONDISI KEDUA (TRUE)
    hasil = angka_1 - angka_2
    print(f"\nHasilnya adalah {hasil}")
elif operator == "*": ##KONDISI KETIGA (TRUE)
    hasil = angka_1 * angka_2
    print(f"\nHasilnya adalah {hasil}")
elif operator == "/": ##KONDISI KEEMPAT (TRUE)
    hasil = angka_1 / angka_2
    print(f"\nHasilnya adalah {hasil}")
else: ##KONDISI FALSE
    print("ERROR404")
print("END PROGRAM")