## PENGENALAN LIST / CARA MEMBUAT LIST
# note = dalam list, kita dapat memasukan data berupa tipe string, boolean dan integer
# kumpulan data angka (numbers)
data_angka = [1,5,2,3]
print(data_angka)

# kumpulan data string
data_string = ["sakha", "pratama", "justin"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1, "sakha", True]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # 0 = mulai dari 0, 10 = sampai sebelum sepuluh, 2 = kelipatan 2 // range(start,stop,step)
print(data_range)
data_list = list(data_range) # mengcasting range dengan membuat variabel penampung list()
print(data_list)

# list comprehension = membuat list dengan for loop
list_wfor = [i**2 for i in range(0,10)] 
print(list_wfor)

# membuat list menggunakan for dan list
# range pada looping jika menggunakan list, hasilnya akan sama saat menggunakan variable penampung ataupun tidak
list_wforif = [i for i in range(0,10) if i != 5] # tidak menggunakan variable penampung
print(list_wforif)

data = range(0,10) # menggunakan variable penampung
list_wforif2 = [i for i in data if i != 5] # jika bertemu angka 5, maka tidak akan di print
print(list_wforif2)

# menampilkan list genap menggunakan for dan if
data = range(0,10)
list_wforif2 = [i**2 for i in data if i%2 == 0] # setiap angka yang dimodulus oleh 2 hasil nya 0, maka akan genap
print(list_wforif2)

# menampilkan list ganjil menggunakan for dan if
data = range(0,10)
list_wforif2 = [i**2 for i in data if i%2 == 1] # setiap angka yang dimodulus oleh 2 hasil nya 1, maka akan ganjil
print(list_wforif2)

    

