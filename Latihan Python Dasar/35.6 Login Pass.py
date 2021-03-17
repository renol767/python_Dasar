from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+"a.txt",'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    user_entry.delete(0,END)
    pass_entry.delete(0,END)

    Label(screen1,text =  'Registrasi Sukses', fg = 'green', font = {'Calibri',11}).pack()
def Login():
    global screen
    global username
    global password
    global user_entry
    global pass_entry
    screen = Toplevel(screen)
    screen.title('Login')
    screen.geometry('400x350')
    username = StringVar()
    password = StringVar()

    Label(screen, text='Login', ).pack()
    Label(screen, text='').pack()
    Label(screen, text='Username').pack()
    user_entry = Entry(screen, textvariable=username)
    user_entry.pack()
    Label(screen, text='').pack()
    Label(screen, text='Password').pack()
    pass_entry = Entry(screen, textvariable=password)
    pass_entry.pack()
    Label(screen, text='').pack()
    Label(screen, text='').pack()
    Button(screen, text='Login', width='15', height='1', font={'Calibri', 11}).pack()
def Regist():
    global screen1
    global username
    global password
    global nama
    global user_entry
    global pass_entry
    global nama_entry
    screen1 = Toplevel(screen)
    screen1.title('Registrasi')
    screen1.geometry('400x350')
    username = StringVar()
    password = StringVar()
    nama = StringVar()

    Label(screen1, text = 'Isi Form Registrasi Berikut',).pack()
    Label(screen1, text = '').pack()
    Label(screen1, text = 'Nama Lengkap').pack()
    nama_entry = Entry(screen1, textvariable = nama)
    nama_entry.pack()
    Label(screen1, text='').pack()
    Label(screen1, text = 'Username').pack()
    user_entry = Entry(screen1, textvariable = username)
    user_entry.pack()
    Label(screen1, text='').pack()
    Label(screen1, text = 'Password').pack()
    pass_entry = Entry(screen1, textvariable = password)
    pass_entry.pack()
    Label(screen1, text='').pack()
    Label(screen1,text = '').pack()
    Button(screen1,text = 'Register',width = '15',height = '1', font = {'Calibri',11},command = register_user()).pack()
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('400x350')
    screen.title('LOGIN PAGE 1.0')
    Label(text = 'LOGIN PAGE 1.0', bg = 'grey', width = '300', height = '2', font = {'Calibri',11}).pack()
    Label(text = '').pack()
    Button(text = 'Login', width = '30',height = '2',command = Login()).pack()
    Label(text = '').pack()
    Button(text = 'Registrasi',width = '30',height = '2', command = Regist()).pack()
    screen.mainloop()
main_screen()
