# return
a = 8
def kuadrat (a):
    total = a**2
    print("Kuadrat dari",a,"adalah",total)
    return total
a = kuadrat(a)
print (a)
print (50*'-')
# return multiple argument
def tambah (a,b):
    total = a+b
    print(a, "+" , b , '=', total)
    return total
def kali (a,b):
    total = a*b
    print(a, "x" , b , "=", total)
    return total
a = tambah(3,8)
b = kali (2,tambah(7,8))
print(a)
print(b)
# function dengan lambda
kali = lambda x,y : x*y
print("Lambda Funct : ",kali(3,5))
