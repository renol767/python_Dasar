# Stacks And Queues
# Stacking
hp = [1,2,3,4,5,6,7,8]
print("data cek 1",hp)

# nambah data
hp.append(9)
hp.append(10)
print("data cek 2",hp)

# menghapus data paling belakang
out=hp.pop()
print("data yang dihapus :",out)
print("data cek 3",hp)
print(90*"-")
# Queuing
from collections import deque

antrian = deque([1,2,3,4,5])
# menambah data memakai append
# menghapus data paling kiri/awal
out = antrian.popleft()
print(antrian)
print(out)
out = antrian.popleft()
print(antrian)
print(out)