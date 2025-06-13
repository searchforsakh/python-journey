## operasi pada list
data_angka = [1,2,3,4,5,2,3,4,8,4,2,2,1,4,5,6,7,8,0]
print(f"data angka = {data_angka}")

## OPERASI COUNT = MENGHITUNG BANYAKNYA ITEM PADA DATA LIST (MENGGUNAKAN VARIABLE PENAMPUNG)
data_count2 = data_angka.count(2) #sintaks = .count(item yang ingin dihitung jumlahnya/banyaknya)
print(f"banyaknya angka 2 adalah = {data_count2}")
data_count8 = data_angka.count(8) #sintaks = .count(item yang ingin dihitung jumlahnya/banyaknya)
print(f"banyaknya angka 8 adalah = {data_count8}")

## OPERASI INDEX = MENGAMBIL POSISI ITEM PADA DATA LIST (MENGGUNAKAN VARIABLE PENAMPUNG)
data = ["Jussa", "Proff", "Preman", "Bang Jay"]
index_proff = data.index("Proff") #sintaks = .index(item yang ingin diambil posisinya/indexnya)
print(f"item ini berada pada posisi/index {index_proff} dalam list")
index_preman = data.index("Preman") 
print(f"item ini berada pada posisi/index {index_preman} dalam list")

# OPERASI SORT = MENGURUTKAN ITEM ANGKA(int) atau HURUF(str) PADA DATA LIST (TANPA MENGGUNAKAN VARIABLE PENAMPUNG)
# OPERASI REVERSE = MEMBALIK URUTKAN ITEM ANGKA(int) atau HURUF(str) PADA DATA LIST (TANPA MENGGUNAKAN VARIABLE PENAMPUNG) # JIKA INGIN DATA BERURUTAN GUNAKAN SORT TERLEBIH DAHULU SETELAH ITU REVERSE
print(f"data angka sebelum di sort/diurutkan\t= {data_angka}")
data_angka.sort()
print(f"data angka setelah si sort/diurutkan\t= {data_angka}")
data_angka.reverse()
print(f"data angka setelah di reverse\t\t= {data_angka}")

print(f"data str sebelum di sort/diurutkan\t= {data}")
data.sort()
print(f"data str setelah di sort/diurutkan\t= {data}")
data.reverse()
print(f"data setelah di reverse\t\t\t= {data}")

