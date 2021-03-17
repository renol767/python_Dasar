# ada 2 tipe eror, eror syntax(bisa dideteksi complier),eror output
# Try and Exception
# bilangan apapun yang dibagi 0 maka akan eror tetapi jika memakai try and except maka akan tidak eror
try :
    a = 1/0
except :
    print("Not Eror")
while True:
    try :
        an = int(input("Masukan Angka Penyebut: "))
        am = int(input("Masukan Angka Pembilang: "))
        hasil = an/am
        break
    except Exception as eror :
        print("Eror Nya Adalah\n", eror) #kita print apa yang eror(sayangnya dalam bahasa inggris :()
    # satu lagi except nama eror nya
    # Division by zero,ValueError,Import Error,IOError,EOFError,Keyboard Interupted,dll
print("Hasil : ", hasil)
# Jadi ketika kita memasukan huruf(bukan Angka) biasa nya program akan eror, tetapi jika kita memakai
# try and except maka ketika kita memasukan huruf maka akan keluar tulisan "Yang anda masukan bukan angka"