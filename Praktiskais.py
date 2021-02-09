#Importejam tkinter un hashlib bibliotekas
from tkinter import filedialog
from tkinter import *
import hashlib
import os

#Definejam ievadi
def ievade():
    global mape
    mape = StringVar()
    mape = filedialog.askdirectory(initialdir = "/", title = "Izvelies mapi!")
    os.chdir(mape)
    faili = os.listdir('.')

    #sakam salidzinasanu
    dublikati = []
    hash_keys = dict()
    for index, filename in  enumerate(faili):
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
            if filehash not in hash_keys: 
                hash_keys[filehash] = index
            else:
                dublikati.append(filename)
        
    if not dublikati:
        Label (logs, text =  ("Tika parbaudita mape:", mape)) \
            .grid(row = 4, column = 0)
        Label (logs, text = "Identiski faili netika atrasti", \
            font = "none 20 bold") .grid(row = 5, column = 0)
    else:
        for d in dublikati:
            Label (logs, text =  ("Tika parbaudita mape:", mape)) \
                .grid(row = 4, column = 0)
            Label (logs, text =  ("Tika atrasti dublikati:", d), \
                font = "none 20 bold") .grid(row = 5, column = 0)
#Loga parametri
logs = Tk()
logs.title("Mans praktiskais darbs Python")
logs.configure(background="black")
#logs.geometry("500x500")
#bilde
bilde = PhotoImage(file="magni.gif") 
Label (logs, image = bilde, bg = "black") \
    .grid(row = 0, column = 0 )
#teksts
teksts1 = Label(logs, text="Identisku failu parbaude - ludzu izvelieties mapi!", \
        bg = "black", fg = "white", font = "none 20 bold") \
            .grid(row = 1, column = 0)

#foldera izvele
poga = Button(logs, text = "Izveleties mapi", font = "none 25 bold", \
        pady = 20, padx = 15, highlightbackground='black', command = ievade) \
            .grid(row = 2, column = 0)

#turam logu valja
logs.mainloop()