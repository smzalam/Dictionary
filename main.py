# https://rapidapi.com/community/api/urban-dictionary
# https://rapidapi.com/dpventures/api/wordsapi

from tkinter import *
from test import getWordDef
from tkinter import scrolledtext, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo as si
import pandas as pd

class App():
    def __init__(self, root):
        self.root = root
        self.menu()
        self.homepage()
        self.hidden = 0

    def menu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Home",command=self.openhomepage)
        # self.menu.add_command(label="All-in-one",command=self.openaonepage)
        self.menu.add_command(label="Definition", command=self.opendefpage)
        self.menu.add_command(label="Synonyms", command=self.opensynpage)
        self.menu.add_command(label="Antonyms", command=self.openantpage)
        self.menu.add_command(label="File", command=self.openfilepage)    
          
    def homepage(self):
        
        self.l = Label(root, text="Home", fg = "#e67017", font="Vedana 48 bold")
        self.l.place(x=250, y = 20)
        
        self.about = Button(root, text="About", command=self.about_click, font=(None, 20), width=15, bg="#FFFFFF")
        self.about.place(x=100, y = 180)

        self.credits = Button(root, text="Credits", command=self.credit_click, font=(None, 20), width=15, bg="#FFFFFF")
        self.credits.place(x=360, y=180)
        
    def defpage(self):

        self.l = Label(root, text="Dictionary", fg = "#e67017", font="Vedana 32 bold")
        self.l.place(x=250, y = 20)
        self.e = Entry(root, width=40, font=(None, 15))
        self.e.place(x=140, y = 100)

        self.b = Button(root, text="Enter", command=self.button_click, font=(None, 10), width=15)
        self.b.place(x=300, y=140)
        
    def synpage(self):
        self.l = Label(root, text="Synonyms", fg = "#26c9b4", font="Vedana 32 bold")
        self.l.place(x=250, y = 20)
        self.e = Entry(root, width=40, font=(None, 15))
        self.e.place(x=140, y = 100)

        self.b = Button(root, text="Enter", command=self.button_click, font=(None, 10), width=15)
        self.b.place(x=300, y=140)
    
    def antpage(self):
        self.l = Label(root, text="Antonyms", fg = "#db273c", font="Vedana 32 bold")
        self.l.place(x=250, y = 20)
        self.e = Entry(root, width=40, font=(None, 15))
        self.e.place(x=140, y = 100)

        self.b = Button(root, text="Enter", command=self.button_click, font=(None, 10), width=15)
        self.b.place(x=300, y=140)
    
    def aonepage(self):
        self.l = Label(root, text="Encyclopedia", fg = "#4e0487", font="Vedana 32 bold")
        self.l.place(x=230, y = 20)
        self.e = Entry(root, width=40, font=(None, 15))
        self.e.place(x=140, y = 100)

        self.b = Button(root, text="Enter", command=self.button_click, font=(None, 10), width=15)
        self.b.place(x=300, y=140)
    
    def filepage(self):
        self.filelabel = Label(root, text="Words in Excel Sheet", fg="#1ba848", font="Vedana 32 bold")
        self.filelabel.place(x=150, y=20)
        
        self.instructions = Button(root, text="Instructions", command=self.file_instructions,bg="#FFFFFF", font=(None, 20), width=15)
        self.instructions.place(x=100, y=180
                                )
        self.open_dialog = Button(root, text="Open Excel File", command=self.openFile, font=(None, 20), width=15, bg="#FFFFFF")
        self.open_dialog.place(x=360, y=180)
   
    def openhomepage(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
        self.homepage()
    
    def opendefpage(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
        
        self.defpage()
        
    def opensynpage(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
            
        self.synpage()
            
    def openantpage(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
            
        self.antpage()
            
    def openaonepage(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
            
        self.aonepage()
        
    def openfilepage(self):
        for widget in self.root.winfo_children():
            widget.place_forget()

        self.filepage()

    def button_click(self):
        print(self.e.get())
        definitions = getWordDef(self.e.get())
        self.l = 1
        self.text =  scrolledtext.ScrolledText(root, wrap=WORD, height=8, width=80)
        self.text.place(x=20, y = 180)
        for i in definitions:
            self.text.insert(END, "Definition " + str(self.l) + ": " + i + "\n\n")
            self.l += 1
    
    def about_click(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
            
        self.label = Label(root, text="About", fg="#443278", font="Vedana 32 bold")
        self.label.place(x=290, y=20)
        self.back_button = Button(root, text="Back", command=self.openhomepage, font=(None, 10), width=10, bg="#FFFFFF")
        self.back_button.place(x=100, y=35)
        self.about_label = Label(root, text="This is a dictionary.\nYou can search words by definition, synonyms, or antonyms.\nYou also have the option to upload an excel file full of words and the program will fill it out.", fg="#000000", font="Vedana 12")    
        self.about_label.place(x=50, y=150)
    
    def credit_click(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
            
        self.label = Label(root, text="Credits", fg="#783264", font="Vedana 32 bold")
        self.label.place(x=270, y=20)
        self.back_button = Button(root, text="Back", command=self.openhomepage, font=(None, 10), width=10, bg="#FFFFFF")
        self.back_button.place(x=100, y=35)
        self.about_label = Label(root, text="Credit to the following STANDS4 APIS: \n Dictionary \n Synonyms \n Antonyms", fg="#000000", font="Vedana 12")    
        self.about_label.place(x=200, y=150)
   
    def file_instructions(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
            
        self.label = Label(root, text="Instructions", fg="#443278", font="Vedana 32 bold")
        self.label.place(x=290, y=20)
        self.back_button = Button(root, text="Back", command=self.openfilepage, font=(None, 10), width=10, bg="#FFFFFF")
        self.back_button.place(x=100, y=35)
        self.about_label = Label(root, text="This is a dictionary.\nYou can search words by definition, synonyms, or antonyms.\nYou also have the option to upload an excel file full of words and the program will fill it out.", fg="#000000", font="Vedana 12")    
        self.about_label.place(x=50, y=150)
            
    def openFile(self):
        filetypes = (
            ('Excel', '*.csv'),
            ('Excel', '*.xls'),
            ('Excel', '*.xlsx')
        ) 
        
        filename = fd.askopenfilename(
            title = "Open Excel Sheet",
            initialdir = '/',
            filetypes = filetypes
        )
        
        if filename:
            try:
                filename = r"{}".format((filename))
                self.df = pd.read_excel(filename)
                
                si (
                    title='Selected File',
                    message=filename
                )
            
            except ValueError:
                si (
                    title="ValueError",
                    message="File could not be opened. Please check if it is the correct file type."
                )
        
        self.treeview()
        
    def treeview(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
        self.treeframe = Frame(root, width=700, height=400)
        self.treeframe.pack(expand=False)
        self.tree = ttk.Treeview(self.treeframe, selectmode="browse")
        self.clear_tree()
        self.yscrollbar = ttk.Scrollbar(self.treeframe, orient=VERTICAL, command=self.tree.yview)
        self.xscrollbar = ttk.Scrollbar(self.treeframe, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=self.yscrollbar.set)
        self.tree.configure(xscroll=self.xscrollbar.set)
        self.yscrollbar.pack(side="right", fill='y')
        self.xscrollbar.pack(side='bottom', fill='x')
        
        self.counter = 0
        for i in self.df.columns:
            self.counter += 1
        
        self.column_width = self.root.winfo_width() //self.counter
        
        self.tree["column"] = list(self.df.columns)
        self.tree["show"] = "headings"
        for column in self.tree["column"]:
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor=CENTER, width=self.column_width)
            
        self.df_rows=self.df.to_numpy().tolist()
        for row in self.df_rows:
            self.tree.insert("", "end", values=row)
        
        self.tree.pack(side="left")
        
        
    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())
      
            
root = Tk()
app = App(root)
root.geometry("700x400")
root.resizable(width=False , height=False)


root.mainloop()