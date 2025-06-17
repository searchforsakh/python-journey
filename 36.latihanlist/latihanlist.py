list_buku = []
while True:
    print("\nMasukkan data buku...\n")
    judul = input("masukkan judul buku\t = ")
    penulis = input("masukkan penulis\t = ")

    data_buku = [judul,penulis]
    list_buku.append(data_buku)
    print("\n"+"="*25)
    for index, data in enumerate(list_buku):
        print(f"{index+1} | {data[0]} | {data[1]}")
        
    print("\n"+"="*25)
    inputuser = input("Lanjut mendata ? (y/n)\t = ")
    if inputuser == "n":
        break
