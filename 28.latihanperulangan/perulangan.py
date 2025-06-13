# 1. menggunakan for
x = 1
for i in range(4): # range untuk menentukan seberapa banyak baris
    print("#"*x) # jika menggunakan variabel iterator(i) pada aksi, maka range akan dihitung dari 0. jika ingin range dari angka 1, maka harus membuat variabel penampung baru untuk pengganti variable iterator, contoh (x = 1)
    x += 1
print("END FOR")

# 2. menggunakan while loop
x = 1
while True:
    print("#"*x)
    x += 1

    if x > 4:
        break
print("END WHILE LOOP")

# 3. print jika ganjil
x = 1
while True:
    if x%2: # kondisi pengecekan --> jika hasilnya 1, maka aksi true akan berjalan, jika hasilnya selain 1, maka aksi false akan berjalan
        print("#"*x) # aksi true dari kondisi if
        x += 1

    else: # else adalah aksi false dari kondisi if
        x += 1
        continue # meng-skip semua sintaks yang ada dibawahnya, dan akan menuju ke kondisi pertama (while True:)

    if x > 10:
        break
print("akhir ganjil")

# 4.membuat segitiga bagian atas
x = 1 # x adalah jumlah pengulangan
y = 10 # y adalah jumlah range
spasi = int(y/2) # spasi adalah jumlah spasi 
while True:
    if x%2: # kondisi pengecekan --> jika hasilnya 1, maka aksi true akan berjalan, jika hasilnya selain 1, maka aksi false akan berjalan
        print(" "*spasi, "#"*x) # aksi true dari kondisi if
        spasi -= 1
        x += 1

    else: # else adalah aksi false dari kondisi if
        x += 1
        continue # meng-skip semua sintaks yang ada dibawahnya, dan akan menuju ke kondisi pertama (while True:)

    if x > y:
        break
print("akhir segitiga bagian atas")

# dari ai
# Inisialisasi variabel
sisi = 9  # Harus angka ganjil untuk hasil yang sempurna
spasi = sisi // 2  # Mulai dengan setengah sisi untuk spasi
count = 1  # Baris pertama dimulai dari 1 simbol #

# Bagian Atas Belah Ketupat
while count <= sisi:
    print(" " * spasi + "#" * count)
    spasi -= 1  # Mengurangi spasi untuk baris berikutnya
    count += 2  # Menambah jumlah karakter '#' setiap baris dengan 2

# Reset variabel untuk Bagian Bawah
spasi = 1  # Spasi dimulai dari 1
count = sisi - 2  # Mengurangi jumlah karakter '#' agar tidak duplikat garis tengah

# Bagian Bawah Belah Ketupat
while count > 0:
    print(" " * spasi + "#" * count)
    spasi += 1  # Menambah spasi untuk baris berikutnya
    count -= 2  # Mengurangi jumlah karakter '#' setiap baris dengan 2
print("akhir belah ketupat (ai)")


# hasil dari mereverse segitiga keatas (ngulik sendiri)
# membuat segitiga keatas
count = 1 # count adalah jumlah pengulangan
sisi = 10 # sisi adalah jumlah range
spasi = int(sisi/2) # spasi adalah jumlah spasi 
while True:
    if count%2==1: # kondisi pengecekan --> jika hasilnya 1, maka aksi true(if) akan berjalan, jika hasilnya selain 1, maka aksi false(else) akan berjalan
        print("#"*spasi, "="*count) # aksi true dari kondisi if
        spasi -= 1
        count += 1

    else: # else adalah aksi false dari kondisi if
        count += 1
        continue # meng-skip semua sintaks yang ada dibawahnya, dan akan menuju ke kondisi pertama (while True:)
    
    if count > sisi:
        break
# membuat segitiga kebawah
sisi = 1
count = 10
spasi = int(count/6) 
while True:
    if count%2==1: # kondisi hasilnya akan 1/ganjil maka akan melakukan print
        print("#"*spasi, "="*count)
        count -= 1
        spasi += 1
    else:
        count -= 1
        continue
    if count < sisi:
        break
print("akhir belah ketupat(reverse bagian atas segitiga)")