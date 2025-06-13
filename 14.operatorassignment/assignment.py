# operasi yang dapat dilakukan dengan penyigkatan
# operasi ditambah dengan assignmnet

print("\n====(+)(-)(*)(/)(**)====") 
a = 5 # adalah assignment
print("nilai a: ", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi: ", a)  

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi: ", a)  

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi: ", a)  

a /= 2 # artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi: ", a)  

a **= 3 # eksponen
print("nilai a **= 3, nilai a menjadi: ", a)  

print("\n====(%)(//)====") # modulus dan floor division
b = 10
print("Nilai b: ", b)

b %= 3
print("nilai b %= 3, nilai b menjadi: ", b) 

b = 10
print("Nilai b: ", b)

b //= 3
print("nilai b //= 3, nilai b menjadi: ", b)

print("\n====(|)(&)(^)====") # operasi bitwise OR, AND, XOR
## OR (jika salah satu True, maka hasilnya adalah True)
c = True
print("Nilai C: ", c)
c |= False
print("nilai c |= False, nilai c menjadi: ", c)
c = False
print("Nilai C: ", c)
c |= False
print("nilai c |= False, nilai c menjadi: ", c)

## AND (jika salah satu False, maka hasilnya adalah False)
c = True
print("\nNilai C: ", c)
c &= False
print("nilai c &= False, nilai c menjadi: ", c)
c = True
print("Nilai C: ", c)
c &= True
print("nilai c &= True, nilai c menjadi: ", c)

## XOR (^) (akan true jika salah satu true, sisanya false)
c = True
print("\nNilai C: ", c)
c ^= False
print("nilai c ^= False, nilai c menjadi: ", c)
c = True
print("Nilai C: ", c)
c ^= True
print("nilai c ^= True, nilai c menjadi: ", c)

print("\n====(>>)(<<)====") # Shifting
## Shift right (>>) menggeser bit ke kanan
## Shift left (<<) menggeser bit ke kiri
c = 0b00101000
print("Nilai c: ", format(c, '08b'))
c >>= 3
print("nilai c >>= 3, nilai c menjadi: ", format(c, '08b'))
c <<= 5
print("nilai c <<= 5, nilai c menjadi: ", format(c, '08b'))