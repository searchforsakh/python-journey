# MENGOPERASIKAN LIST >> data = ["sakha", 1, True]
# 1.MENGAMBIL DATA DARI LIST >> variabel = data[posisi index]
# 2.MENGHITUNG JUMLAH DATA DALAM LIST >> variabel = len(data)
# 3.MENAMBAHKAN item pada list sesuai posisi >> data.insert(posisi, item yg ingin ditambah)
# 4.MENAMBAH item di akhir list >> data.append(item yg ingin ditambah)
# 5.MENGGABUNGKAN DUA BUAH LIST >> data_lama.extend(data_baru)
# 6.MERUBAH ITEM PADA DATA LIST
# 7.MEREMOVE DATA
# 8.MEREMOVE DATA TERAKHIR

# index   0/-3      1/-2       2/-1   --> posisi/index
data = ["Justin", "Ragnar", "Verdonk"]

# MENGAMBIL DATA DARI LIST
data0 = data[0]
print(f"data pertama (index ke 0) = {data0}")

data_terakhir = data[-1]
print(f"data terakhir (index ke -1) = {data_terakhir}")

# MENGHITUNG JUMLAH DATA DALAM LIST
jumlah_data = len(data) # len = properti bawaan dari python untuk menghitung jumlah item dalam list data
print(f"banyaknya item dalam data adalah {jumlah_data}")

## MANIPULASI DATA LIST = MERUBAH DATA DARI LIST
print(f"data sebelum dirubah\t\t\t= {data}")

# MENAMBAHKAN item pada list sesuai posisi (TIDAK MENGGUNAKAN VARIABLE PENAMPUNG)
data.insert(2, "Jay") #sintaks = insert(posisi, item(yang ingin ditambah))
print(f"penambahan item di tengah list\t\t= {data}")

# MENAMBAH item di akhir list (TIDAK MENGGUNAKAN VARIABLE PENAMPUNG)
data.append("Ridho") #sintaks = append(item yang ingin ditambah)
print(f"penambahan item di akhir list\t\t= {data}")

print(f"data setelah dirubah\t\t\t= {data}")

# MENGGABUNGKAN DUA BUAH LIST
data_baru = ["Nathan", "Marsel", "Ole"]
data.extend(data_baru) #sintaks = data_lama.extend(data_baru)
print(f"data setelah digabung dengan data baru\t= {data}")

# MERUBAH ITEM PADA DATA LIST
data[2] = "Paes" #merubah data kedua(jay) menjadi paes
print(f"data setelah item ke dua diganti\t= {data}")

# MEREMOVE DATA
data.remove("Verdonk") #akan error jika hurufnya tidak sesuai
print(f"data setelah di remove\t\t\t= {data}")

# MEREMOVE DATA TERAKHIR
data_pop = data.pop() #PROPERTY POP BISA MENGGUNAKAN VARIABLE PENAMPUNG UNTUK MELIHAT ITEM YANG DIHILANGKAN
print(f"data setelah item terakhir di remove\t= {data}")
print(f"data yang dihilangkan\t\t\t= {data_pop}")


