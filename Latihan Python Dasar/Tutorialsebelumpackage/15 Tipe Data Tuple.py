#list(bisa nambah data)
ganjil = [1,3,5,7,9,11]
#tuple(tidak bisa nambah data)
genap = (2,4,6,8,10,12)
ganjil[2] = 99
# eror genap[2] = 99
ganjil.append(2)
# error genap.append(3)
# genap itu bisa memekai count dan index
print(ganjil)
print(genap)
#tuple itu lebih sedikit menggunakan memori dan lebih cepat di proses nya
#pembuktian:
import sys
data_list = [1,3,5,7,9,11]
data_tuple = (2,4,6,8,10,12)
memori_datalist = sys.getsizeof(data_list)
memori_datatuple = sys.getsizeof(data_tuple)
print("Memori Digunakan : ", memori_datalist)
print("Memori Digunakan : ", memori_datatuple)
import timeit
waktu_datalist = timeit.timeit(stmt= "[1,3,5,7,9,11]")
waktu_datatuple = timeit.timeit(stmt= "(2,4,6,8,10,12)")
print("Waktu Memproses nya : ",waktu_datalist)
print("Waktu Memproses nya : ",waktu_datatuple)

