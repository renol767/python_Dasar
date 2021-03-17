# init adalah sebuah func yang keluar pertama/paling awal ketika dipanggil
class mahasiswa ():
    def __init__(self,name,nim):
        self.nama = name
        self.nim = nim
    def kelas(self,kel):
        print(self.nama, "Berada Di Kelas", kel)
    def jurusan(self):
        print(self.nama, "Jurusan Teknik Informatika")
renol = mahasiswa('Renol Nindi Kara N', 1903027)

print(renol.nama)
print(renol.nim)
renol.kelas('D3TI1A')
renol.jurusan()