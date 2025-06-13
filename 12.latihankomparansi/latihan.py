# membuat gabungan area rentang dari angka

# ++++++++++3-----------10++++++++++
print("\n++++++++++3-----------10++++++++++")
inputUser = float(input("masukkan angka yg bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# +++++++++3---------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3: ", isKurangDari) 

# --------------10+++++++++++
# memriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10: ", isLebihDari) 

# ++++++++++3-----------10++++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan adalah: ",isCorrect)


# ---------3+++++++++++10-------------
print("\n---------3+++++++++++10-------------")
# kasus irisan
inputUser = float(input("masukkan angka yg bernilai lebih dari 3\ndan\nkurang besar dari 10\n:"))

# ------------------3++++++++++++
#memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3:", isLebihDari)

#+++++++++++++10-----------------
#memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10:", isKurangDari)

# ---------3+++++++++++10-------------
isCorrect = isLebihDari and isKurangDari
print("angka yg anda masukkan adalah:", isCorrect)