# Agar Atribut di dalam class tidak bisa diubah dari luar kasih "__namanya"
class mahasiswa ():
    __kampus = "Politeknik Negeri Indramayu" # Gak Bisa Diubah Di Public/Dari Luar
    def __init__(self,name,nim):
        self.nama = name #public
        self.nim = nim #public
    def kampus(self):
        print(self.__kampus)
    def kelas(self,kel):
        print(self.nama, "Berada Di Kelas", kel)
    def jurusan(self):
        print(self.nama, "Jurusan Teknik Informatika")
renol = mahasiswa('Renol Nindi Kara N', 1903027)
renol.kampus() # __kampus dipanggil/di print
print(renol.nama)
print(renol.nim)
renol.kelas('D3TI1A')
renol.jurusan()
