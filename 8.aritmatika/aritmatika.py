a = 10
b = 3

#operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)
# print("data=", hasil,"type=", type(hasil))

#operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)
# print("data=", hasil,"type=", type(hasil))

#operasi perkalian *
hasil = a * b
print(a,'*',b,'=', hasil)
# print("data=", hasil,"type=", type(hasil))

#operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)
# print("data=", hasil,"type=", type(hasil))

#operasi eksponen (pangkat) **
hasil = a ** b #a pangkat b = 10 pangkat 3
print(a,'**',b,'=', hasil)
# print("data=", hasil,"type=", type(hasil))

#operasi modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil)
# print("data=", hasil,"type=", type(hasil))

#operasi floor division (pembagian dibulatkan kebawah) //
hasil = a // b
print (a,'//',b,'=', hasil)
# print("data=", hasil, "type=", type(hasil))

print("=================================")
#prioritas operasi, operational precedence
'''
1. ()
2. exponen(pangkat) **
3. perkalian pembagian dll * / ** % //
4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)

#kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)
