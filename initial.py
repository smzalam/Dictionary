# https://rapidapi.com/community/api/urban-dictionary
# https://rapidapi.com/dpventures/api/wordsapi

from tkinter import *
from test import getWordDef
from tkinter import scrolledtext    


root = Tk()
root.geometry("700x400")
root.resizable()

w = Frame(root, width=700, height=100, bg="blue")
w.pack()

def button_click():
    print(e.get())
    definitions = getWordDef(e.get())
    l = 1
    text =  scrolledtext.ScrolledText(root, wrap=WORD, height=8, width=80)
    text.place(x=20, y = 180)
    for i in definitions:
        text.insert(END, "Definition " + str(l) + ": " + i + "\n\n")
        l += 1






menu = Menu(root)
menu.add_command(label="Definition")
menu.add_command(label="Synonyms")
menu.add_command(label="Antonyms")
menu.add_command(label="All-in-one")
menu.add_command(label="File")
root.config(menu=menu)

l = Label(root, text="Dictionary", fg = "#e67017", font="Vedana 32 bold")
l.place(x=250, y = 20)
e = Entry(root, width=40, font=(None, 15))
e.place(x=140, y = 100)

b = Button(root, text="Enter", command=button_click, font=(None, 10), width=15)
b.place(x=300, y=140)

root.mainloop()