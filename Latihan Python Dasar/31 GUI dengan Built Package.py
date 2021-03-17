#salah satu package build in di python yaitu tkinter(Gui nya python) (graphical user interface)
import tkinter

main_window = tkinter.Tk()

def event_tekan ():
    label2 = tkinter.Label(main_window, text = "Saya Ga suka ditekan Hmph :/")
    label2.pack()

label = tkinter.Label(main_window, text = "Hallo World \nIni adalah GUI(Graphic User Interface")
tombol = tkinter.Button(main_window, text = 'Tekan Untuk Keluar', command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()
