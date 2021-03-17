def userx():
    user = input("Masukan Username : ")
    if user == 'admin':
        print("Lanjut Gan, Masukin Passwordnya")
        pw = input("Masukan Password : ")
        if pw == 'admin':
            print("Login Sukses !")
        else:
            print("Password salah!")
    else:
        print("Salah Coy Usernamenya")
        return userx()
userx()