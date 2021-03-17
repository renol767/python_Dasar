# Method adalah class yang didalamnya mempunyai func,if,dsb
class mahasiswa ():
    nama = 'nama'
    def kelas(self,kel):
        print(self.nama, "Berada Di Kelas", kel)
    def jurusan(self):
        print(self.nama, "Berada di jurusan Teknik Informatika")
renol = mahasiswa()
kira = mahasiswa()

renol.nama = 'Renol Nindi Kara N'
kira.nama = "Kira Light Yagami"

renol.kelas("A")
kira.jurusan()