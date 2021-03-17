# Nilai Awal Akhir Jika Awal < Akhir Maka ++, Begitupun Sebaliknya
x = int(input("Nilai Awal : "))
y = int(input("Nilai Akhir : "))

if x<=y:
    while x<=y:
        print(x)
        x += 1
    else :
        print("Selesai")
if x>=y:
    while x>=y:
        print(x)
        x -= 1
    else :
        print("Selesai")
