# COPY LIST DIGUNAKAN KETIKA KITA AKAN MERUBAH DATA/MENCOPYNYA, MAKA GUNAKAN PROPERTY .copy(). (harus menggunakan variable penampung / variable baru)

a = ["ragnar","calvin","haye"]
print(f"a = {a}")

b = a # pass by reference (tidak disrankan untuk mencopy data)
print(f"b = {b}")

# akan merubah member dari a
# langkah dibawah akan merubah kedua list, dikarenakan id hex dari kedua list tersebut sama (harus menggunakan property .copy())
a[-1] = "jay"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# mengeluarkan address dari list a dan b
print(f"address dari list a = {hex(id(a))}")
print(f"address dari list b = {hex(id(b))}\n")

# menduplikat list dengan copy --> tujuannya adalah mendapatkan isi dari list yg ingin dicopy, tetapi dengan id hex/address yang berbeda
# caranya dengan menambahkan variable penampung terlebih dahulu
print("Membuat list c dengan a.copy()") # --> full duplikat / membuat data baru
c = a.copy() # --> menghasilkan isi list yang sama dengan list a, tetepi dengan id hex/address yang berbeda. sehingga, ketika mengubah list c, list a tidak akan ikut berubah
c[1] = "jusa"
a[2] = "ivar" 
print(f"a = {a}") 
print(f"b = {b}")
print(f"c = {c}")
# hasil dari list a dan b akan sama, karena list tersebut masih dalam satu address/hex id
print(f"address dari list a = {hex(id(a))}")
print(f"address dari list b = {hex(id(b))}")
print(f"address dari list c = {hex(id(c))}")

a = ["sakha", "budi", "pais"]
b = a.copy() # .copy() = akan membuat list baru yang sama seperti list a, tanpa merubah list a
b[2] = "reyes" # menambahkan reyes di index 2
b.append("rizki") # menambahkan rizki akhir data
b.insert(1,"nabila") #menambahkan nabila di index 1
b.remove("sakha") # menghapus sakha
b.pop() # menghapus data terakhir
print(f"a = {a}")
print(f"b = {b}")
