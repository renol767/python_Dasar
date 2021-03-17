nilai = int(input("Nilai Mu : "))

print("Nilai MAHASISWA")
if nilai == 100:
    print("Perfect")
if 80 <= nilai <= 100:
    print("A")
elif 70 <= nilai < 80:
    print("B")
elif 60 <= nilai < 70:
    print("C")
elif 40 <= nilai < 60:
    print("D")
elif 0 <= nilai < 40:
    print("E")

print(100*"=")

#IF untuk String Bukan Angka

gorengan=["bakwan","tempe","gehu","cireng","cau"]
beli = str(input("Gorengan apa ? "))
if beli in gorengan:
    print("Mamanx Bilang",beli,"Masih Banyak + Haraneut")
else:
    print("Punten Bahasa Naon eta")