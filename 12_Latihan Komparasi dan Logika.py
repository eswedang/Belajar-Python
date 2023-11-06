#a = 10
#b = 6
#results = a // b
#print(results)

# Membuat Gabungan Area Rentang Dari Angka
#+++++++++3-------------10++++++++++
userinput = float(input("Masukkan angka kurang dari 3\natau\nlebih dari 10\n:"))

#Memeriksa angka kurang dari 3
isKurangDari = (userinput < 3)
print("Kurang dari 3 =", isKurangDari)

#Memeriksa angka lebih dari 10
isLebihDari = (userinput > 10)
print("Lebih dari 10 =", isLebihDari)

#++++++3------10+++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan=", isCorrect)

#-------3+++++10--------- (irisan)
print("\n",10*"=","\n")
userinput = float(input("Masukkan angka lebih dari 3\ndan\nkurang dari 10\n:"))

#Lebih dari 3
isLebihDari = (userinput > 3)
print("Lebih dari 3 =", isLebihDari)

#Kurang dari 10
isKurangDari = (userinput < 10)
print("Kurang dari 10 =", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan=", isCorrect)