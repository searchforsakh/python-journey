empty_list = []
while True:
    print("masukan data buku")
    judul = input("masukkan judul buku = ")
    penulis = input("masukkan penulis = ")

    data_buku = [judul, penulis]
    empty_list.append(data_buku) # --> list kosong akan ditambah dari setiap data yang dimasukkan
    print(empty_list)

