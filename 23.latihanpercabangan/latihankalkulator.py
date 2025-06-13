print("latihan kalkulator") # menggunakan if else karena hanya memiliki satu jawaban
angka1 = float(input("Masukkan angka pertama = "))
operator = input("Masukkan operasi hitung +, -, /, * = ")
angka2 = float(input("Masukkan angka kedua = "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil perhitungan = {hasil}")
if operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil perhitungan = {hasil}")
if operator == "/":
    hasil = angka1 / angka2
    print(f"Hasil perhitungan = {hasil}")
if operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil perhitungan = {hasil}")
else:
    print("operator salah")
print("program selesai")