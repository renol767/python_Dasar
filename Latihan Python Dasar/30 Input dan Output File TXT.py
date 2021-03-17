#w = write text / menulis dan menghapus file lama, jika tidak ada file lama maka akan dibuat file baru
#r = hanya bisa dibaca
#a = menambah data di akhir baris
#r+ = write and read mode

# Membuat Text baru
file = open("30 Data.txt",'w') #kenapa w?karena saya blm punya data sebelumnya/harus membuat baru
file.write("Test")
file.write("\nTest 2")
file.write("\nTest 3")
file.close() #Jangan lupa TUTUP !!!
# Membaca File Text
file2 = open('30 Data.txt','r')
#print(file2.read()) #cek output
print(file2.readline())#hanya membaca baris ke 1
file2.close()
# Menambah text di akhir baris
file3= open('30 Data.txt', 'a')
print(file3.write("\nNambah"))
file3.close()