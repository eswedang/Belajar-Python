print(12000)

#operasi aritmatika
a = 2
b = 4

#operasi tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

#operasi kurang -
hasil = a - b
print(a,"-",b,"=",hasil)

#operasi kali *
hasil = a * b
print(a,"*",b,"=",hasil)

#operasi bagi /
hasil = a / b
print(a,"/",b,"=",hasil)

#operasi eksponen(pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

#operasi modulus % (sisa pembagian)
hasil = a % b
print(a,"%",b,"=",hasil)

#operasi floor division // (pembulatan pembagian)
hasil = a // b
print(a,"//",b,"=",hasil)

##prioritas operasi, operational precedence
x = 3
y = 2
z = 4
hasil = x ** y + z - x / z * y // x
print(x, '**', y, '+', z, '-', x, '/', z, '*', y, '//', x, '=', hasil)