print("coba")
#a = 10, a adalah variabel dengan nilai 10
#tipe data: Angka Satuan(integer)
data_integer = 1
print(type(data_integer))
print("data :", data_integer)
print("- bertipe :", type(data_integer))

#tipe data: Angka dengan koma(float)
data_float = 1.5
print(type(data_float))
print("data :", data_float)
print("- bertipe :", type(data_float))

#tipe data: Kumpulan karakter(string)
data_string = "Indonesia"
print(type(data_string))
print("data :", data_string)
print("- bertipe :", type(data_string))

#tipe data: biner True or False(boolean)
data_bool = True
print(type(data_bool))
print("data :", data_bool)
print("- bertipe :", type(data_bool))

#tipe data khusus
#bilangan kompleks
data_complex = complex(5,6)
print(type(data_complex))
print("data :", data_complex)
print("- bertipe :", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double, c_char, c_long
data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe :", type(data_c_double))
