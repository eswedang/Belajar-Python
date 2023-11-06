#inpo = input("Siapa kamu?")
#print("Aku adalah",inpo)

#--Operasi Komparasi--#

#setiap hasil komparasi adalah boolean
#<, >, <=, >=, ==, !=, is, is not

a = 4
b = 2

#lebih besar dari >
hasil = a > 3
print(a,'>',3,'=',hasil)
#
#
#
#'is' sebagai sebagai komparasi object identity
x = 5
y = 5
print('nilai x =',x,'id =',hex(id(x)))
print('nilai y =',y,'id =',hex(id(y)))
hasil = x is y
print("x == y =", hasil)
