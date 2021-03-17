# Mewariskan Apa yang Ada di Class Gojek ke Class Grab Secara Secpat (Inheritance)
class gojek():

    def __init__(self,nama,motor,daerah):
        self.nama = nama
        self.motor = motor
        self.daerah = daerah
    def cekid (self):
        print('Nama = ',self.nama,'\nMotor = ' ,self.motor, '\nDaerah = ', self.daerah)
class grab(gojek):
    pass

ojek1 = gojek('Babang tamvan','Astrea','Cirebon')
ojek2 = grab('Andika','Matic','Majalengka')

ojek1.cekid()
ojek2.cekid()