#soal 1 = "------0++++++5------8+++++11-------"
#soal 2 = "++++++0------5++++++8-----11+++++++"

#nomor 1: 
#angka = int(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10:"))

#hasil = 0<angka<5 or 8<angka<11
#print ("Hasil :",hasil)

#nomor 2: 
#angka = int(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10:"))

#hasil = angka<0 or 5<angka<8 or 11<angka
#print ("Hasil :",hasil)

print("GABUNGAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData >= 0 and InputData <= 5)
print(Angka1)

Angka2 = (InputData >= 8 and InputData <= 11)
print(Angka2)

Hasilnya = Angka1 or Angka2
print("Answer :",Hasilnya)

print("IRISAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData <= 0 or InputData >= 5)
print(Angka1)

Angka2 = (InputData <= 8 or InputData >= 11)
print(Angka2)

Hasilnya = Angka1 and Angka2
print("Answer :",Hasilnya)