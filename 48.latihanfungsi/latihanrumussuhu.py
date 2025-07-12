# membuat rumus penghitung suhu

# header 
def header():
    import os
    os.system("cls")
    print(f"{"Membuat rumus penghitung suhu":^50}")
    print(f"{"^"*40:^50}")

def inputusercelcius():
    celcius = int(input("Masukkan Suhu dalam Celcius = "))
    return celcius
def inputuserreamur():
    reamur = int(input("Masukkan Suhu dalam reamur = "))
    return reamur
def inputuserfahrenheit():
    fahrenheit = int(input("Masukkan Suhu dalam fahrenheit = "))
    return fahrenheit
def inputuserkelvin():
    kelvin = int(input("Masukkan Suhu dalam kelvin = "))
    return kelvin

def celciustoreamur(celcius):
    return 4/5*celcius
def celciustofahrenheit(celcius):
    return 9/5*celcius+32
def celciustokelvin(celcius):
    return celcius+273

def reamurtocelcius(reamur):
    return 5/4*reamur
def reamurtofahrenheit(reamur):
    return 9/4*reamur+32
def reamurtokelvin(reamur):
    return 5/4*reamur +273

def fahtocelcius(fahrenheit):
    return 5/4*(fahrenheit-32)
def fahtoreamur(fahrenheit):
    return 4/9*(fahrenheit-32)
def fahtokelvin(fahrenheit):
    return 5/9*(fahrenheit-32)+273

def kelvintocelcius(kelvin):
    return kelvin-273
def kelvintoreamur(kelvin):
    return 4/5*(kelvin-273)
def kelvintofahrenheit(kelvin):
    return 9/5*(kelvin-273)+32

def display(message1,message2,value):
    print(f"Hasil dari {message1} ke {message2} adalah {value} ")
# def pilihcelcius():
#     int(input("Ingin dirubah kemana? 1.reamur 2.fahrenheit 3.kelvin"))
while True:
    header()
    # opsi2 = pilihcelcius()
    opsi = int(input("""
Masukkan Pilihan Konversi Suhu
1. Celcius
2. Reamur
3. Fahrenheit
4. Kelvin
= """))
    

    if opsi == 1:
        print(f"\nPilihan anda = {opsi}")
        celcius = inputusercelcius()
        toreamur = celciustoreamur(celcius)
        tofahrenheit = celciustofahrenheit(celcius)
        tokelvin = celciustokelvin(celcius)
        display("Celcius", "Reamur", toreamur)
        display("Celcius", "fahrenheit", tofahrenheit)
        display("Celcius", "kelvin", tokelvin)

    elif opsi == 2:
        print(f"\nPilihan anda = {opsi}")
        reamur = inputuserreamur()
        tocelcius = reamurtocelcius(reamur)
        tofahrenheit = reamurtofahrenheit(reamur)
        tokelvin = reamurtokelvin(reamur)
        display("Reamur", "Celcius", tocelcius)
        display("Reamur", "fahrenheit", tofahrenheit)
        display("Reamur", "kelvin", tokelvin)

    elif opsi == 3:
        print(f"\nPilihan anda = {opsi}")
        fahrenheit = inputuserfahrenheit()
        tocelcius = fahtocelcius(fahrenheit)
        toreamur = fahtoreamur(fahrenheit)
        tokelvin = fahtokelvin(fahrenheit)
        display("Fahrenheit", "Celcius", tocelcius)
        display("Fahrenheit", "Reamur", toreamur)
        display("Fahrenheit", "Kelvin", tokelvin)

    elif opsi == 4:
        print(f"\nPilihan anda = {opsi}")
        kelvin = inputuserkelvin()
        tocelcius = kelvintocelcius(kelvin)
        toreamur = kelvintoreamur(kelvin)
        tofahrenheit = kelvintofahrenheit(kelvin)
        display("Kelvin", "Celcius", tocelcius)
        display("Kelvin", "Reamur", toreamur)
        display("Kelvin", "Fahrenheit", tofahrenheit)

    else:
        print("Masukkan Sesuai Nomor diatas!")
        pass

    iscontinue = input("Apakah Ingin Lanjut? (y/n) = ")
    if iscontinue == "n":
        break

print("PROGRAM SELESAI, TERIMAKASIH.")
