## Bitwise = Operasi pada masing masing Bit.

a = 5
b = 9

#bitwise OR (|)
c = a | b
print("\n==========OR==========")
print("Nilai: ", a, "Binary: ", format(a, '08b'))
print("Nilai: ", b, "Binary: ", format(b, '08b'))
print("---------------------(|)")
print("Nilai: ", c, "Binary: ", format(c, '08b'))

#bitwise AND (&)
c = a & b
print("\n==========AND==========")
print("Nilai: ", a, "Binary: ", format(a, '08b'))
print("Nilai: ", b, "Binary: ", format(b, '08b'))
print("---------------------(&)")
print("Nilai: ", c, "Binary: ", format(c, '08b'))

#bitwise XOR (^)
c = a ^ b
print("\n==========XOR==========")
print("Nilai: ", a, "Binary: ", format(a, '08b'))
print("Nilai: ", b, "Binary: ", format(b, '08b'))
print("---------------------(^)")
print("Nilai: ", c, "Binary: ", format(c, '08b'))

#bitwise NOT (~)
c = ~a #Not akan melakukan miroring mulai dari -1 
print("\n==========NOT==========")
print("Nilai: ", a, "Binary: ", format(a, '08b'))
print("---------------------(~)")
print("Nilai: ", c, "Binary: ", format(c, '08b'))
print("---------------------(^)") #gunakan xor untuk mengflip bitnya
d = 0b0000001001
e = 0b1111111111
print("Nilai: ", e^d, "Binary: ", format(e^d, '08b'))

##shifting
#Shift right (>>)
c = a >> 2 # menggeser bit ke kanan sebanyak dua kali
print("\n==========>>==========")
print("Nilai: ", a, "Binary: ", format(a, '08b'))
print("---------------------(>>)")
print("Nilai: ", c, "Binary: ", format(c, '08b'))

#Shift left (<<)
c = a << 2 # menggeser bit ke kiri sebanyak dua kali
print("\n==========<<==========")
print("Nilai: ", a, "Binary: ", format(a, '08b'))
print("---------------------(<<)")
print("Nilai: ", c, "Binary: ", format(c, '08b'))

# a = 5
# b = 8
# c = a | b
# d = a & b
# e = a ^ b 

# print("\n=========OR========")
# print("Nilai: ", a, "Binary: ", format(a, '08b'))
# print("Nilai: ", b, "Binary: ", format(b, '08b'))
# print("------------------(|)")
# print("Nilai: ", c, "Binary: ", format(c, '08b'))

# print("\n=========And========")
# print("Nilai: ", a, "Binary: ", format(a, '08b'))
# print("Nilai: ", b, "Binary: ", format(b, '08b'))
# print("------------------(&)")
# print("Nilai: ", d, "Binary: ", format(d, '08b'))

# print("\n=========XOR========")
# print("Nilai: ", a, "Binary: ", format(a, '08b'))
# print("Nilai: ", b, "Binary: ", format(b, '08b'))
# print("------------------(^)")
# print("Nilai: ", e, "Binary: ", format(e, '08b'))

# f = ~a
# print("\n=========NOT========")
# print("Nilai: ", a, "Binary: ", format(a, '08b'))
# print("------------------(~)")
# print("Nilai: ", f, "Binary: ", format(f, '08b'))

