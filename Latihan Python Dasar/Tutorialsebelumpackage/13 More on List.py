# More on list
barang = ['kunci','ember','gayung','selang','spons']

# Menambah data di dalam list
barang.append('sabun')
print(barang)
# atau bisa juga
barang.append('busa')
print(barang)
# Membuat List Ke Bawah
for i in barang:
    print(i)
# Memasukan barang / insert
barang.insert(2,'sabun')
print(barang)
# Menghitung barang sabun ada berapa
x=barang.count('sabun')
print(x)
# Remove barang yang di temui pertama kali
barang.remove('sabun')
print(barang)
# Membalikan Urutan Nama Barang
barang.reverse()
print(barang)
# Mengubah barang agar tidak mengubah public variable (Lihat Output)
stuff = barang.copy()
stuff.append('Pasta')
print(stuff)
print(barang)