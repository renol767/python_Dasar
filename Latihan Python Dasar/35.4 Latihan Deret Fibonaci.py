suku = int(input('Masukan Suku Ke Berapa : '))
a = 0
b = 1
c = 3
print(a)
print(b)
while c <= suku:
    c = a+b
    a = b
    b = c
    print(c)
    c+=1
