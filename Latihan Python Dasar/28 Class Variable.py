# class
class mahasiswa ():
    kampus = "Politeknik Negeri Indramayu" # public/bisa di ubah dari luar
    jmlmhs = 0
    def __init__(self,name,nim):
        self.nama = name #public
        self.nim = nim #public
        mahasiswa.jmlmhs += 1
# Main Program
renol = mahasiswa('Renol Nindi Kara N',1903027)
kira = mahasiswa('Steven kira',1903028)
aceng = mahasiswa('Aceng Pilek',1903029)
renol.kampus = "Politeknik Negeri Majalengka" #kita ubah kampus milik renol
renol.nim = 1001 # ubah nim nya
aceng.kampus = "Politeknik Negeri Malang" #ubah kampus milik aceng

print(mahasiswa.kampus)
print(renol.__dict__) #kita cek data milik renol (nim,kampus)
print(kira.__dict__) #bandingkan denhgan yang di atas
print(aceng.__dict__)
print(mahasiswa.jmlmhs)