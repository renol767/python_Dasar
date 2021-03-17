# global dan local scope
# mengubah variable local
namakucing = 'brangbrang'
makanan = 'whiskas'
def namabaru (a):
    namakucing = a
    print("Nama Kocheng Baru Saya Adalah", namakucing)
namabaru('jarwo')
print('nama kucing lama saya',namakucing)
# mengubah variable global
def makan (a,b):
    global namakucing,makanan
    namakucing = a
    makanan = b
makan('Ketie','Ikan')
print("Nama kucing saya adalah", namakucing, 'makanan nya',makanan)