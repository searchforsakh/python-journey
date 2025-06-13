# Tugas Komparansi

# 1.------0++++++5--------8++++++++11-------
print("\nNo.1 ------0++++++5--------8++++++++11-------")
inputUser = float(input("Masukkan angka yang ingin di uji:"))
print("\nAngka yang anda Masukkan: ", inputUser)

# ------0++++++
# memeriksa angka lebih dari 0
isLebihDari0 = inputUser > 0
print("Lebih dari 0: ", isLebihDari0)

# ++++++5------
# memeriksa angka kurang dari 5
isKurangDari5 = inputUser < 5
print("Kurang dari 5: ", isKurangDari5)

# ------8++++++
# memeriksa angka lebih dari 8
isLebihDari8 = inputUser > 8
print("Lebih dari 8: ", isLebihDari8)

# ++++++11-------
# memeriksa angka kurang dari 11
isKurangDari11 = inputUser < 11
print("Kurang dari 11: ", isKurangDari11)

isCorrect = isLebihDari0 and isKurangDari5 or isLebihDari8 and isKurangDari11
print("Nilai yang anda masukkan adalah: ", isCorrect)

# 2.++++++0-------5+++++++8--------11+++++++
print("\nNo.2 ++++++0-------5+++++++8--------11+++++++")
inputUser = float(input("Masukkan angka yang ingin di uji:"))
print("\nAngka yang anda Masukkan: ", inputUser)

# +++++0------
isKurangDari0 = inputUser < 0
print("Kurang dari 0: ", isKurangDari0)

# -----5+++++
isLebihDari5 = inputUser > 5
print("Lebih dari 5: ", isLebihDari5)

# ++++++8-----
isKurangDari8 = inputUser < 8
print("Kurang dari 8: ", isKurangDari8)

# -----11+++++
isLebihDari11 = inputUser > 11
print("Lebih dari 11: ", isLebihDari11)

isCorrect = isKurangDari0 or isLebihDari5 and isKurangDari8 or isLebihDari11
print("Nilai yang anda masukkan adalah: ", isCorrect)
