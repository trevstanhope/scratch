from Tkinter import *

class ScrolledText(Frame):
    def __init__(self, parent=None, text="", file=None, side=TOP):
        Frame.__init__(self, parent)
        self.pack(side=side, expand=YES, fill=BOTH)
        self.createWidgets()
        self.clear()

    def createWidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

    def clear(self):
        self.setText("")

    def setText(self, text="", file=None):
        if file: 
            text = open(file, 'r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()

    def getText(self):
        return self.text.get('1.0', END+'-1c')

    def addText(self, text="",file=None):
        if file:
            text = open(file, 'r').read()
        self.text.insert(END, text)
        self.text.mark_set(INSERT, END)
        #self.text.focus()

    def see(self, index):
        self.text.see(index)