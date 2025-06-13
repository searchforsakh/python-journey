# nested list = menggabungkan beberapa list menjadi satu dengan membuat variable penampung baru yang beranggotakan list tersebut
# jika ingin membuat list didalam list, maka komponennya adalah list itu sendiri
data0 = [1,2]
data1 = [3,4,5]

data_list_biasa = [1,2,3,4]
print(f"data biasa\t= {data_list_biasa}")

data_list2D = [data0,data1]
print(f"data list 2D\t= {data_list2D}")

#contoh penggunaan --> untuk membuat list menjadi lebih kompleks
peserta0 = ["Ragnar", 3, "Fc Dender"]
peserta1 = ["Justin", 0, "Wolves"]
peserta2 = ["Verdonk", 0, "NEC"]
peserta3 = ["Haye", 3, "Almere"]

list_peserta = [peserta0,peserta1,peserta2,peserta3]
print(f"list Peserta Gabungan = {list_peserta}")

for i in list_peserta:
    print(f"Nama pemain = {i[0]}") # --> mengambil index ke 0 atau data pertama dari list_peserta
    print(f"Jumlah gol = {i[1]}")
    print(f"Asal Klub = {i[2]}\n")

# akan ada masalah dengan references (next vid)