#program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPRATUR\n")


print("=====CELCIUS=====")
celcius = float(input("Masukkan suhu dalam celcius: "))
print("suhu adalah",celcius, "celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah:", reamur, "reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah:", fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah:", kelvin, "kelvin")


print("\n=====REAMUR=====")
reamur = float(input("Masukkan suhu dalam reamur:"))
print("suhu adalah:",reamur,"reamur")

#celcius
celcius = (5/4) * reamur    
print("suhu dalam celcius adalah:", celcius, "celcius")

#fahrenheit
fahreinheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit:", fahrenheit, "Fahrenheit")

#kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah:", kelvin, "kelvin")


print("\n=====FAHRENHEIT=====")
fahrenheit = float(input("masukkan suhu dalam fahrenheit:"))
print("suhu adalah:", fahrenheit, "fahrenheit")

#celcius
celcius = (5/9) * (fahrenheit - 32)
print("suhu dalam celcius adalah:", celcius, "celcius")

#reamur
reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam reamur adalah:", reamur, "reamur")

#kelvin
kelvin = (5/9) * (fahrenheit - 32) + 273
print("suhu dalam kelvin:", kelvin, "kelvin")


print("\n=====KELVIN=====")
kelvin = float(input("masukkan suhu dalam kelvin:"))
print("suhu adalah:", kelvin, "kelvin")

#celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah:", celcius, "celcius")

#reamur
reamur = (4/5) * (kelvin - 273)
print("suhu dalam reamur adalah:", reamur, "reamur")

#fahrenheit
fahrenheit = (9/5 * (kelvin - 273)) + 32
print("suhu dalam fahrenheit adalah:", fahrenheit, "fahrenheit")