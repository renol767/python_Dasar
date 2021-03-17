num = int(input("Masukan Bilangan :"))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, 'bukan bilangan prima')
        else:
            print(num,'adalah bilangan prima')
        break