from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("small project - watch")

def time():
    string = strftime('%I:%M %p')
    label.config(text=string)
    label.after(1000,time)

label = Label(root, font=('Ink-Free',80), background="black", foreground="cyan")
label.pack(anchor="center")


time()
mainloop()