# Tidak, for merupakan pengulangan yang termasuk dalam couted loop. Perulangan for digunakan untuk mengulang suatu proses yang jumlah perulangannya sudah diketahui. 
# PROPERTY YANG SUDAH DIPELAJARI SEJAUH INI
"""
1. print()
2. input()
3. type()
4. format(a, '08b') --> a = variable penampung --> memformat variable(int) menjadi angka biner
5. bin(angka) --> angka = variable penampung --> untuk mengeluarkan angka biner dari variable (int)
6. oct(angka) --> angka = variable penampung --> untuk mengeluarkan angka octal dari variable
7. hex(angka) --> angka = variable penampung --> untuk mengeluarkan address dari variable (str/int)
8. .isalpha() >> untuk mengcek apakah semuanya huruf?
9. .isalnum() >> untuk mengecek apakah semuanya huruf dan angka?
10. .isdecimal() >> untuk mengcek apakah semuanya angka?
11. .isspace() >> untuk mengecek apakah ada spasi, tab, newline(\n)
12. .istitle() >> untuk mengecek apakah semua kata dimulai dengan huruf besar
13. .upper() >> untuk merubah semua str menjadi huruf besar
14. .lower() >> untuk merubah semua str menjadi huruf kecil
15. .isupper() >> untuk mengecek apakah str dalam variable penampung memiliki huruf besar semua
16. .islower() >> untuk mengecek apakah str dalam variable penampung memiliki huruf kecil semua
17. range(start, stop, step) >> menentukan panjang looping 
18. .insert() >> MENAMBAHKAN item pada list sesuai posisi (TIDAK MENGGUNAKAN VARIABLE PENAMPUNG)
19. .append() >> MENAMBAH item di akhir list (TIDAK MENGGUNAKAN VARIABLE PENAMPUNG)
20. .extend() >> MENGGABUNGKAN DUA BUAH LIST
21. .remove() >> meremove data
22. .pop() >> meremove data terakhir
23. .




## penggabungan komponen join() split()
pisah = ['Sakha','pratama','sakha']
print(pisah)
gabung = ', '.join(pisah)
print(gabung)

gabung = '---'.join(pisah)
print(gabung)

gabung = "Ragnar Oratmangoen"
print(gabung.split(" "))

## alokasi karakter rjust(), ljust(), center()
print("\nalokasi karakter rjust(), ljust(), center()")
kanan = "Calvin".rjust(20,'=') # membuat rata kanan
print("*"+ kanan +"*")

kiri = "verdonk".ljust(20,'~') # membuat rata kiri
print("(" + kiri + ")")

tengah = "Calvin".center(20,'<') # membuat rata tengah
print(":" + tengah + ":")

#kebalikannya >> strip()

tengah = "Calvin".strip('<') # menghilangkan tanda '<'
print(":" + tengah + ":")



"""

# angka = 123
# print(f"format 1 = {(format(angka,'08b'))}")
# print(f"format 2 = {(bin(angka))}")