print("REMEMBER: gunakan (+), jika menggabungkan string dengan string")
print("REMEMBER: gunakan (,), jika didalam variabel tidak ada string\n")

## METHOD OPERATOR
# operator dalam bentuk method

# merubah case dari string

# merubah semua ke upper case
a = "Kevin Diks"
print("Normal: " + a)
a = a.upper()
print("Upper: " + a)

# merubah semua ke lower case
b = "Thom Haye"
print("Normal: " + b)
b = b.lower()
print("lower: " + b)

print("\n=====pengecekan dengan isX method=====")
## pengecekan dengan isX method = islower/isupper

# contoh untuk pengecekan lower case
c = "ragnar oratmangoen"
apakah_lower = c.islower() # hasilnya akan bool
# print("ragnar oratmangoen is lower? " + str(apakah_lower))
format_str = f"ragnar oratmangoen is lower? {apakah_lower}"
print(format_str)


# contoh untuk pengecekan upper case
c = "ragnar oratmangoen"
apakah_upper = c.isupper() # hasilnya akan bool
# print("ragnar oratmangoen is upper? " + str(apakah_upper))
format_str = f"ragnar oratmangoen is upper? {apakah_upper}"
print(format_str)

# isalpha() >> untuk mengcek apakah semuanya huruf?
# isalnum() >> untuk mengecek apakah semuanya huruf dan angka?
# isdecimal() >> untuk mengcek apakah semuanya angka?
# isspace() >> untuk mengecek apakah ada spasi, tab, newline(\n)
# istitle() >> untuk mengecek apakah semua kata dimulai dengan huruf besar

# isalpha()
contoh = "sakhapratama" #spasi akan dinilai false 
cek_isalpha = contoh.isalpha() # hasil nya bool
print("sakha pratama is alpha? " + str(cek_isalpha))

# isalnum()
contoh = "kevindiks2" #spasi akan dinilai false
cek_isalnum = contoh.isalnum() # hasil nya bool
print("kevindiks2 is alnum? " + str(cek_isalnum))

# isdecimal()
contoh = "12345678" #spasi akan dinilai false
cek_isdecimal = contoh.isdecimal() # hasil nya bool
print("12345678 is decimal? " + str(cek_isdecimal))

# isspace()
contoh = "           " # selain spasi, tab, newline(\n). akan dinilai false
cek_isspace = contoh.isspace() # hasil nya bool
print("            is space? " + str(cek_isspace))

# istitle()
contoh = "The Energy Never Dies" #spasi tidak berpengaruh
cek_istitle = contoh.istitle() # hasil nya bool
print("The Energy Never Dies is title? " + str(cek_istitle))


## mengecek komponen startwith endswith
cek_start = "Sakha Pratama".startswith("Sakha")
print("Sakha is Startwith? " + str(cek_start))

cek_end = "Justin Hubner".endswith("Hubner")
print("Hubner is Endswith? " + str(cek_end))

print()

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



