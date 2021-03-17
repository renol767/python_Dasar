from random import randint
Janken = ['Batu','Gunting','Kertas']
com = Janken[randint(0,2)]
me = input("Pilihan Anda : ")
if  me == com:
    print("Seri")
elif me == 'Batu':
    if com == 'Kertas':
        print("Kamu Kalah",me,'Sedangkan Komputer',com)
    else:
        print("Kamu Menang", me, 'Sedangkan Komputer', com)
elif me == 'Kertas':
    if com == 'Gunting':
        print("Kamu Kalah",me,'Sedangkan Komputer',com)
    else :
        print("Kamu Menang", me, 'Sedangkan Komputer', com)
elif me == 'Gunting':
    if com == 'Batu':
        print("Kamu Kalah", me, 'Sedangkan Komputer', com)
    else :
        print("Kamu Menang", me, 'Sedangkan Komputer', com)
else:
    print("Ges Ulah Ngasupken Nu Aneh Aneh Babyk")