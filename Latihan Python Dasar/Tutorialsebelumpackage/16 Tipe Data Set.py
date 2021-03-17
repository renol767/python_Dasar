# tipe data set / himpunan : ketika ada nama/angka yang sama maka dianggap 1, tidak punya urutan
superhero = {"wiro sableng", "gundala", "gatot kaca" , "superman"}
superhero.add("batman")
superhero.add("superman")
# cek output maka superman cuman ada 1
print(superhero)
# KELEBIHAN
ganjil = {1,3,5,7,9,11}
genap = {2,4,6,8,10,12}
prima = {2,3,5,7}
print(ganjil.union(genap)) # kalau ada yang sama tidak ditulis
print(ganjil.intersection(prima)) # kalau ada yang sama ditulis
