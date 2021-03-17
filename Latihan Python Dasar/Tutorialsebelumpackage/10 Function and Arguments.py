nama = str(input("Siapa Nama Nya : "))
def mahasiswa ():
    print("Nama Nya Adalah",nama)
mahasiswa()
def kelas(nama,kelas):
    print("Siswa ini Di Kelas",kelas)
    print("Wali Kelas nya",nama)
kelas(nama="3M4N",kelas="3")
def pengawas(ruang,nama='Rani',galak='tidak'):
    print("Ruang : ",ruang)
    print("Nama Pengawas",nama)
    print("Galak ? ",galak)
pengawas(13)
pengawas(19,nama='Entin',galak='iya')
#pengawas(nama='mul',galak='tidak') # Eror Karena ruang tidak memiliki argument
