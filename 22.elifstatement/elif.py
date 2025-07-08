## ELIF = Else If Statement
# SINTAKS
# if kondisi:
#     aksi True
# elif kondisi:
#     aksi True
# elif kondisi:
#     aksi True

nama = input("Masukkan nama anda = ")
if nama == "Ragnar": # kondisi 1
    print("Halo Wak Haji!") # aksi true 1
elif nama == "Verdonk": # kondisi 2
    print("Halo Loopy!") # aksi true 2
elif nama == "Rafa":
    print("Halo El Klemer!")
elif nama == "Justin":
    print("Halo JUSSA!")
else:
    print("IDK THIS GUY PLS REPORT")
print("End Program")

nilai = int(input('Masukkan nilai: '))
if nilai >= 90:
  print('Predikat A')
elif nilai >= 80:
  print('Predikat B')
elif nilai >= 60:
  print('Predikat C')
elif nilai >= 40:
  print('Predikat D')
else:
  print('Predikat E')

# gunakan elif untuk program yang memiliki kemungkinan jawaban lebih dari satu
# gunakan if else untuk program yg memiliki jawaban satu