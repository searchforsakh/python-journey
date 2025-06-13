# format string

### contoh generic
## string
nama = "justin"
format_str = f"Hello {nama}"
print(format_str)

## boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

## angka
# sebelum di format
"""
angka = 2006.5
format_str = "angka = " + str(angka)
print(format_str)
"""
# setelah di format
angka = 2006.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 10
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan {variable:,}
angka = 2000000000000000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal {variable:.3f} >> mengambil 3 angka dibelakang koma (,)
angka = 2006.53456
format_str = f"angka = {angka:.3f}"
print(format_str)

# menampilkan leading zero 
# {angka:010.2f} >> mengambil jumlah/total semua angka, 
# jika kurang/lebih otomatis menampilkan spasi, tambahkan angka (0) agar menampilkan angka 0
angka = 2006.54321
format_str = f"angka = {angka:08.2f}"
print(format_str)

# menampilkan tanda + atau -
# tambahkan {variable:+d} untuk menampilkan tanda (+)/(-)
# tambahkan {variable:+.2f} untuk menampilkan 2 angka dibelakang koma (,) dan tanda (+)
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)

# memformat persen
# tambahkan {varaible:%} untuk mengubahnya menjadi persen
# tambahkan {varaible:.2%} untuk menambahkan 2 angka dibelakang koma (,)
persentase = 17
format_persen = f"persen = {persentase:%}"
print(format_persen)

# melakukan operasi aritmaterika didalam placeholder({})
harga = 10000
jumlah = 15

format_str = f"Total Harga = Rp. {harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexa = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)