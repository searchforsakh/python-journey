# Array awal
my_array = [1, 2, 3, 4, 5]

# Mengubah setiap elemen array menjadi string
string_array = [str(element) for element in my_array]
print(string_array)
# Menggunakan join() untuk menggabungkan elemen string dengan pemisah tertentu (misalnya spasi)
result_string = "#".join(string_array)

# Menampilkan hasilnya
print(result_string)  # Output: 1#2#3#4#5