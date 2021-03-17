spas = ""
bint = "*"
x = 0
while x <= 5:
    kol = x
    while kol <= 5:
        kol += 1
        spas += " "
    bil = 4
    while bil < 5:
        bint += "*"
        bil += 1
    spas=spas+bint+"\n"
    x += 1
print(spas)