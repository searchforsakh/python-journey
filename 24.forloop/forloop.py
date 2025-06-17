# perulangan (loop)

# for kondisi:
#     aksi

# ini dengan list
angka_list = [0,2,4,6,8,10] # ini adalah list
print(angka_list)

for i in angka_list: # untuk i didalam angka_list
    print(f"i sekarang adalah {i}")
print("END PROGRAM1")

# ini dengan range
angka_range = range(11)

for i in angka_range:
    print(f"i sekarang adalah {i}")
print("END PROGRAM2")

angka_range = range(1,10) # dimulai dari 1, diakhiri dengan 10 (10 tidak diambil)

for i in angka_range:
    print(f"contoh{i}")
print("END PROGRAM3")

# ini dengan string (looping data per huruf)
data = "SAKHAAAAAA"
for qwertyhj in data:
    print(f"{qwertyhj}")
print("END PROGRAM4")

