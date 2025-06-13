print("REMEMBER: gunakan (+), jika menggabungkan string dengan string")
print("REMEMBER: gunakan (,), jika didalam variabel tidak ada string\n")

# operasi dan manipulasi string

## 1. menyambung string (concatenate)
nama_pertama = "Justin"
nama_tengah = "Quincy"
nama_akhir = "Hubner"

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_akhir
print("ini nama lengkap JUSA: " + nama_lengkap)

## 2. menghitung panjang string
panjang = len(nama_lengkap) # hasilnya akan int
# print("panjang dari " + nama_lengkap + " = " + str(panjang))
format_str = f"panjang dari nama lengkap = {panjang}"
print(format_str)

## 3. operator untuk string (in/not in)
# mengecek apakah ada komponen char/string di dalam string

d = "Q"
status = d in nama_lengkap 
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "q"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "I"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

## 4. mengulang string
print("WK"*10)
print(9*"WK")

## 5. indexing [](mengambil data dari string,dimulai dari 0)
print("index ke 0: " + nama_lengkap[0])
print("index ke 1: " + nama_lengkap[1])
print("index ke -1: " + nama_lengkap[-1])
print("index ke -2: " + nama_lengkap[-2])
print("index ke [0:4]: " + nama_lengkap[0:5])
print("index ke [4:8]: " + nama_lengkap[4:9])
print("index ke [0,2,4,6,8,10]: " + nama_lengkap[0:11:2])

## 6. item paling kecil
print("paling kecil: " + min(nama_lengkap))

## 7. item paling besar
print("paling besar: " + max(nama_lengkap))

## 8. ASCII CODE
ascii_code = ord(" ")
print("ASCII code untuk spasi: " + str(ascii_code))
data = 117
print("char untuk ASCII 117: " + chr(data))

## 9. operator dalam bentuk method (contoh: .count)
data = "Katarina Stalin"
jumlah = data.count("a")
print("Jumlah a pada data: " + str(jumlah))
# format_str = f"Jumlah a pada data: {jumlah}"
# print(format_str)