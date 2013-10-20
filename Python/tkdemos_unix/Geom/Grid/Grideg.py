from Tkinter import *
from toolbar import Toolbar
import string

sticky_opt = [ N, S, W, E,
               NW, SW, NE, SE, NS, EW,
               NSEW ]


class GridDemoTB(Toolbar):
    def __init__(self, parent, gridFrm):
        self.entry_lst = []
        self.gridFrm = gridFrm
        self.btnCount = 1
        Toolbar.__init__(self, parent)
        self.setTitle("Tkinter grid demo")

    def createWidgets(self):
        Label(self, text="Items", relief=RIDGE).grid(sticky=EW, columnspan=2)
        Label(self, text="Row").grid(row=1)
        Label(self, text="Column").grid(row=1, column=1)
        self.entRow = Entry(self, bg="white", width=5)
        self.entRow.grid(row=2, sticky=EW)
        self.entry_lst.append(self.entRow)
        self.entCol = Entry(self, bg="white", width=5)
        self.entCol.grid(row=2, column=1, sticky=EW)
        self.entry_lst.append(self.entCol)
        Label(self, text="RowSpan").grid(row=3)
        Label(self, text="ColSpan").grid(row=3, column=1)
        self.entRowSpan = Entry(self, bg="white", width=5)
        self.entRowSpan.grid(row=4, sticky=EW)
        self.entry_lst.append(self.entRowSpan)
        self.entColSpan = Entry(self, bg="white", width=5)
        self.entColSpan.grid(row=4, column=1, sticky=EW)
        self.entry_lst.append(self.entColSpan)
        listFrm = Frame(self)
        listFrm.grid(row=5, columnspan=2)
        self.stickyList = Listbox(listFrm, bg="white")
        scroll =  Scrollbar(listFrm, command=self.stickyList.yview)
        self.stickyList.configure(yscrollcommand=scroll.set)
        self.stickyList.grid(row=0, sticky=NSEW)
        scroll.grid(row=0, column=1, sticky=NS)
        self.stickyList.activate(0)
        for opt in sticky_opt:
            self.stickyList.insert(END, string.upper(opt))
        Button(self, text="Create", command=self.createObj).grid(row=6, columnspan=2,sticky=EW)

    def createObj(self):
        try:
            row = int(self.entRow.get())
            if (row < 0):
                row = 0
        except:
            row = 0
        self.entRow.delete(0, END)
        self.entRow.insert(0, "%d" % row)

        try:
            col = int(self.entCol.get())
            if (col < 0):
                col = 0
        except:
            col = 0
        self.entCol.delete(0, END)
        self.entCol.insert(0, "%d" % col)

        try:
            rowspan = int(self.entRowSpan.get())
            if (rowspan < 0):
                rowspan = 0
        except:
            rowspan = 0
        self.entRowSpan.delete(0, END)
        self.entRowSpan.insert(0, "%d" % rowspan)

        try:
            colspan = int(self.entColSpan.get())
            if (colspan < 0):
                colspan = 0
        except:
            colspan = 0
        self.entColSpan.delete(0, END)
        self.entColSpan.insert(0, "%d" % colspan)

	try:
            sticky_index = int(self.stickyList.curselection()[0])
	except:
	    sticky_index = 0
        Button(self.gridFrm, text="-- B%d --" % self.btnCount).grid(row=row,
                                                                    column=col,
                                                                    rowspan=rowspan,
                                                                    columnspan=colspan,
                                                                    sticky=sticky_opt[sticky_index])
	self.btnCount = self.btnCount + 1



root = Tk()
root.title("Tkinter grid demo")

gdtb = GridDemoTB(root, root)

mainloop()
