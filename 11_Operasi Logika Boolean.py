print("Hello,\nWelcome to Python programming.")
#print("coba")
#Operasi Boolean
#not, or, and, xor

print("==========NOT==========")
a = False 
c = not a
print("data a =", a)
print("data c =", c)

#"TRUE" jika salah satu 'true maka hasilnya 'true
print("==========OR==========")
a = True
b = False
c = a or b 
print(a," OR",b,"=",c)
a = True
b = True
c = a or b 
print(a," OR",b," =",c)
a = False
b = True
c = a or b 
print(a,"OR",b," =",c)
a = False
b = False
c = a or b 
print(a,"OR",b,"=",c)

#"AND" jika salah satu 'false maka hasilnya 'false
print("==========AND==========")
a = True
b = False
c = a and b 
print(a," AND",b,"=",c)
a = True
b = True
c = a and b 
print(a," AND",b," =",c)
a = False
b = True
c = a and b 
print(a,"AND",b," =",c)
a = False
b = False
c = a and b 
print(a,"AND",b,"=",c)

#"XOR" jika berbeda maka hasilnya "True"
print("========XOR==========")
a = True
b = False
c = a ^ b 
print(a," XOR",b,"=",c)
a = True
b = True
c = a ^ b 
print(a," XOR",b," =",c)
a = False
b = True
c = a ^ b 
print(a,"XOR",b," =",c)
a = False
b = False
c = a ^ b 
print(a,"XOR",b,"=",c)


