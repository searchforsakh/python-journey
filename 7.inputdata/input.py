#data yang dimasukkan pasti string
Nama = input("masukkan Nama:")
print("nama anda =", Nama, "type =", type(Nama))

#jika ingin mengambil angka, maka:
angka= int(input("Masukkan thn lahir:"))
print("data =", angka, "type =", type(angka))
angka= float(input("Masukkan tinggi badan:"))
print("data =", angka, "type =", type(angka))

#jika ingin mengambil boolean, maka harus diubah ke int/str terlebih dahulu.
biner= bool(int(input("masukkan 1/0:")))
print("data =", biner, "type =", type(biner))
