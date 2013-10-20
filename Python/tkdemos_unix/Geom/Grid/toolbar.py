from Tkinter import *

class Toolbar(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.createWidgets()
    
    def setTitle(self, title):
        self.title(title)
        
    def createWidgets(self):
        pass