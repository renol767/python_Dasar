#sampai (:)
hp = [2,6,53,32,9,10,22,37,97,202]
subhp = hp[:4]
hp1 = [4,89,75,44,67,99,102,201,333,222]

#Mengubah data
hp[4:6] = [62,99]
hp2 = hp,hp1
a = hp2[1][5]

#method list
hp.append(999)
#function list
hp3 = len(hp)
print(hp)
print(subhp)
print("Data", hp+hp1)
print(hp2)
print(a)
print(hp3)