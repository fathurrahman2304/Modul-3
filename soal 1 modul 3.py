# Program menentukan jenis segitiga
print("\n==PROGRAM INI AKAN MENENTUKAN JENIS SEGITIGA BERDASARKAN PANJANG SISI==")
panjang1 = int(input("Masukkan nilai panjang sisi A: "))
panjang2 = int(input("Masukkan nilai panjang sisi B: "))
alas = int(input("Masukkan nilai panjang sisi C: "))
if panjang1 == panjang2 and panjang1 != alas and panjang2 != alas :
    print("ini merupakan segitiga sama kaki")
elif panjang1 == panjang2 == alas:
    print("ini merupakan segitiga sama sisi")
elif panjang1 + panjang2 <= alas or panjang1 + alas <= panjang2 or panjang2 + alas <= alas:
    print("ini bukan segitiga")
else: 
    print("ini segitiga sembarang")

print("--Terima kasih telah menggunakan program saya--")
