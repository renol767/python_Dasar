# while argument:
#       statement:

angka = 0
while angka < 5:
    print("Nilai angka adalah", angka)
    angka = angka+1
start = True # var boolean
angka = 0

while start < 10:
    print(">",angka)
    if angka == 5:
        start = False
        print("Nih Angkanya",angka)
        # bisa pake break,continue,pass
    angka+= 1
    break
else:
    print("Angka sudah ditemukan")
