from Tkinter import *
import tkMessageBox

class App:
    def __init__(self, master, itemtb):
        self.OrgX = 0
        self.OrgY = 0
        toolbar = Frame(master)
        sidebar = Frame(master)
        self.canvas = Canvas(master, bg="white")
        self.CurrObj = None
        self.ShowCurrent = IntVar(master)
        self.itemtb = itemtb

        ##### Create sidebar objects #####
        Label(sidebar, relief=RIDGE, text="TAGS").pack(fill=X)
        self.TagEntry = Entry(sidebar, bg="white")
        self.TagEntry.pack(fill=X)
        Button(sidebar, text="Add", command = self.AddTag).pack(fill=X)
        self.tagList = Listbox(sidebar)
        self.tagList.pack(fill=X)
        Checkbutton(sidebar, text="Show CURRENT", variable=self.ShowCurrent).pack()
        Button(sidebar, text="Remove", command= self.RemoveTags).pack(fill=X)

        sidebar.pack(side=RIGHT, fill=Y)

        ##### Create Toolbar objects #####
        self.MouseCoordsLabel = Label(toolbar, relief=RIDGE, text="   :   ", width=20)
        self.MouseCoordsLabel.pack(side=LEFT)
        self.ReturnValueLabel = Label(toolbar, relief=RIDGE)
        self.ReturnValueLabel.pack(side=LEFT, expand=YES, fill=X)

        toolbar.pack(fill=X)

        ##### Create canvas objects #####
        self.canvas.create_rectangle(40,40,100,120, fill="white")
        self.canvas.create_oval(150, 150, 200, 200, fill="white")
        self.canvas.create_oval(200, 200, 270, 250, fill="white")
        self.canvas.bind("<Button-1>", self.OnCanvasMouseDown)
        self.canvas.bind("<Any-Motion>", self.OnCanvasMouseMove)
        self.canvas.bind("<B1-Motion>", self.OnCanvasMouseDrag)

        self.canvas.pack(expand=YES, fill=BOTH)

    def RefreshTagList(self, lb):
        lb.delete(0, lb.size()-1)
        if (self.CurrObj):
            for t in self.canvas.gettags(self.CurrObj):
                if ((t != CURRENT) or self.ShowCurrent.get()):
                    lb.insert(END, t)

    def AddTag(self):
        if (self.CurrObj):
            self.canvas.addtag_withtag(self.TagEntry.get(), self.CurrObj)
            self.RefreshTagList(self.tagList)
        else:
            tkMessageBox.showerror("Selection", "No selection available")

    def RemoveTags(self):
        if (self.CurrObj):
            for sel_item in self.tagList.curselection():
                self.canvas.dtag(self.CurrObj, self.tagList.get(sel_item))
            self.RefreshTagList(self.tagList)

    def RefreshSel(self):
        self.OnCanvasMouseDown(None)

    # Canvas Mouse events
    # ------------------------------------------------------------------------------------------
    def OnCanvasMouseDown(self, event):
        print "Canvas Mouse Down detected"
        self.canvas.delete("DEL")
        if(event):
            self.OrgX, self.OrgY = event.x, event.y
        for obj in self.canvas.find_all():
            self.canvas.itemconfig(obj, fill="white")
        curr_list = self.canvas.find_withtag(CURRENT)
        if(curr_list):
            self.CurrObj = curr_list[0]
            self.ReturnValueLabel.configure(text="Item ID: %d" % self.CurrObj)
            self.canvas.itemconfig(self.CurrObj, fill="green")
            self.RefreshTagList(self.tagList)
            self.itemtb.UpdateObjInfo(self.canvas, self.CurrObj)
        else:
            self.ReturnValueLabel.configure(text="")
            self.CurrObj = None
            self.itemtb.Clear()
        self.RefreshTagList(self.tagList)

    def OnCanvasMouseMove(self, event):
        self.MouseCoordsLabel.configure(text="%d : %d" % (event.x, event.y))

    def OnCanvasMouseDrag(self, event):
        cur_lst = self.canvas.find_withtag(CURRENT)
        if (cur_lst):
            self.canvas.move(cur_lst[0], event.x - self.OrgX, event.y - self.OrgY)
            self.itemtb.UpdateObjInfo(self.canvas, self.CurrObj)
            self.OrgX, self.OrgY = event.x, event.y
        self.OnCanvasMouseMove(event)

    # ------------------------------------------------------------------------------------------

class FindTB:
    def __init__(self, master, app):
        self.app = app
        Label(master, text="Search",relief=RIDGE).grid(columnspan=4,sticky=NSEW,pady=4)
        self.tagEntry = Entry(master, bg="white")
        self.tagEntry.grid(row=1, columnspan=4)
        Label(master, text="X1").grid(row=2, column=0)
        Label(master, text="Y1").grid(row=2, column=1)
        Label(master, text="X2").grid(row=2, column=2)
        Label(master, text="Y2").grid(row=2, column=3)
        self.x1Entry = Entry(master, bg="white", width=5)
        self.x1Entry.grid(row=3, column=0)
        self.y1Entry = Entry(master, bg = "white", width=5)
        self.y1Entry.grid(row=3, column=1)
        self.x2Entry = Entry(master, bg="white", width=5)
        self.x2Entry.grid(row=3, column=2)
        self.y2Entry = Entry(master, bg="white", width=5)
        self.y2Entry.grid(row=3, column=3)
        Button(master, text="find_above", command=self.fAbove).grid(row=4, columnspan=4,sticky=EW)
        Button(master, text="find_all", command=self.fAll).grid(row=5, columnspan=4,sticky=EW)
        Button(master, text="find_below", command=self.fBelow).grid(row=6, columnspan=4,sticky=EW)
        Button(master, text="find_closest", command=self.fClosest).grid(row=7, columnspan=4,sticky=EW)
        Button(master, text="find_enclosed", command=self.fEnclosed).grid(row=8, columnspan=4,sticky=EW)
        Button(master, text="find_overlapping", command=self.fOverlap).grid(row=9, columnspan=4,sticky=EW)
        Button(master, text="find_withtag", command=self.fWithTag).grid(row=10, columnspan=4,sticky=EW)

    def fAbove(self):
        SelObj = self.app.CurrObj # Keep a reference to CurrObj
        if (SelObj == None):
            tkMessageBox.showerror("Object", "No selection available")
            return ""
        self.app.RefreshSel()     # Will set CurrObj to None
        for item in self.app.canvas.find_above(SelObj):
            self.app.canvas.itemconfig(item, fill="blue")

    def fAll(self):
        self.app.RefreshSel()
        for item in self.app.canvas.find_all():
            self.app.canvas.itemconfig(item, fill="blue")

    def fBelow(self):
        SelObj = self.app.CurrObj
        if (SelObj == None):
            tkMessageBox.showerror("Object", "No selection available")
            return ""
        self.app.RefreshSel()
        for item in self.app.canvas.find_below(SelObj):
            self.app.canvas.itemconfig(item, fill="blue")

    def fClosest(self):
        self.app.RefreshSel()
        try:
            x1 = int(self.x1Entry.get())
            y1 = int(self.y1Entry.get())
        except:
            tkMessageBox.showerror("Coordinates", "Bad coordinates entered")
            return ""
        for item in self.app.canvas.find_closest(x1, y1):
            self.app.canvas.itemconfig(item, fill="blue")
            item_coords = self.app.canvas.coords(item)
            self.app.canvas.create_line(x1, y1, (item_coords[0] + item_coords[2]) / 2,
                                                (item_coords[1] + item_coords[3]) / 2,
                                                tags="DEL", fill="red")

    def fEnclosed(self):
        self.app.RefreshSel()
        try:
            x1 = int(self.x1Entry.get())
            x2 = int(self.x2Entry.get())
            y1 = int(self.y1Entry.get())
            y2 = int(self.y2Entry.get())
        except:
            tkMessageBox.showerror("Coordinates", "Bad coordinates entered")
            return ""
        for item in self.app.canvas.find_enclosed(x1,y1,x2,y2):
            self.app.canvas.itemconfig(item, fill="blue")
        self.app.canvas.create_rectangle(x1, y1, x2, y2,tags="DEL", outline="red")

    def fOverlap(self):
        self.app.RefreshSel()
        try:
            x1 = int(self.x1Entry.get())
            x2 = int(self.x2Entry.get())
            y1 = int(self.y1Entry.get())
            y2 = int(self.y2Entry.get())
        except:
            tkMessageBox.showerror("Coordinates", "Bad coordinates entered")
            return ""
        for item in self.app.canvas.find_overlapping(int(self.x1Entry.get()),
                                                 int(self.y1Entry.get()),
                                                 int(self.x2Entry.get()),
                                                 int(self.y2Entry.get())):
            self.app.canvas.itemconfig(item, fill="blue")
        self.app.canvas.create_rectangle(x1, y1, x2, y2,tags="DEL", outline="red")

    def fWithTag(self):
        self.app.RefreshSel()
        for item in self.app.canvas.find_withtag(self.tagEntry.get()):
            self.app.canvas.itemconfig(item, fill="blue")

class ItemTB:
    def __init__(self, master):
        self.item = None
        self.canvas = None
        self.creators = {"Polygon"   : Canvas.create_polygon,
                         "Rectangle" : Canvas.create_rectangle,
                         "Oval"      : Canvas.create_oval}

        Label(master, text="ITEMS", relief=RIDGE).grid(columnspan=2,pady=4, sticky=EW)
        Label(master, text="x1").grid(row=1, sticky=E)
        Label(master, text="y1").grid(row=2, sticky=E)
        Label(master, text="x2").grid(row=3, sticky=E)
        Label(master, text="y2").grid(row=4, sticky=E)
        Label(master, text="Type").grid(row=5, sticky=E)
        Label(master, text="Width").grid(row=6, sticky=E)
        self.x1Entry = Entry(master, bg="white")
        self.y1Entry = Entry(master, bg="white")
        self.x2Entry = Entry(master, bg="white")
        self.y2Entry = Entry(master, bg="white")
        self.typeLabel = Label(master, bg="white", relief=SUNKEN, anchor=W)
        self.widthEntry = Entry(master, bg="white")
        self.x1Entry.grid(row=1, column=1, sticky=EW)
        self.y1Entry.grid(row=2, column=1, sticky=EW)
        self.x2Entry.grid(row=3, column=1, sticky=EW)
        self.y2Entry.grid(row=4, column=1, sticky=EW)
        self.typeLabel.grid(row=5, column=1, sticky=EW)
        self.widthEntry.grid(row=6, column=1, sticky=EW)
        Button(master, text="Apply", command=self.ApplyToObj).grid(row=7, columnspan=2, sticky=EW)
        Button(master, text="Lift", command=self.LiftObj).grid(row=8, columnspan=2, sticky=EW)
        Button(master, text="Lower", command=self.LowerObj).grid(row=9, columnspan=2, sticky=EW)
        Label(master, text="NEW OBJECT", relief=RIDGE).grid(row=10, columnspan=2, sticky=EW)
        self.NewKind = StringVar(master)
        rb1 = Radiobutton(master, text="Rectangle", variable=self.NewKind, value="Rectangle")
        rb1.grid(row=11, columnspan=2, sticky=W)
        rb2 = Radiobutton(master, text="Oval", variable=self.NewKind, value="Oval")
        rb2.grid(row=12, columnspan=2, sticky=W)
        rb1.select()
        Button(master, text="Create", command=self.CreateObj).grid(row=13, columnspan=2, sticky=EW)

    def EntrySet(self, entry, string):
        entry.delete(0, END)
        entry.insert(0, string)

    def UpdateObjInfo(self, canvas, item):
        coords = canvas.coords(item)
        if (coords):
            self.item = item
            self.EntrySet(self.x1Entry, ("%d" % coords[0]))
            self.EntrySet(self.y1Entry, ("%d" % coords[1]))
            self.EntrySet(self.x2Entry, ("%d" % coords[2]))
            self.EntrySet(self.y2Entry, ("%d" % coords[3]))
            self.typeLabel.configure(text=canvas.type(item))
            self.EntrySet(self.widthEntry, ("%d" % (float(canvas.itemcget(item, "width")))))

    def Clear(self):
        self.item = None
        self.EntrySet(self.x1Entry, "")
        self.EntrySet(self.y1Entry, "")
        self.EntrySet(self.x2Entry, "")
        self.EntrySet(self.y2Entry, "")
        self.typeLabel.configure(text="")
        self.EntrySet(self.widthEntry, "")

    def ApplyToObj(self):
        if (self.canvas == None):
            global instance
            self.canvas = instance.canvas
        if(self.canvas and self.item and self.canvas.find_withtag(self.item)):
            self.canvas.coords(self.item,
                               int(self.x1Entry.get()),
                               int(self.y1Entry.get()),
                               int(self.x2Entry.get()),
                               int(self.y2Entry.get()))
            self.canvas.itemconfig(self.item, width=int(self.widthEntry.get()))
        else:
            tkMessageBox.showerror("Item error", "Item not found on canvas")
            self.Clear()

    def CreateObj(self):
        if (self.canvas == None):
            global instance
            self.canvas = instance.canvas
        func = self.creators[self.NewKind.get()]
        try:
            item = func(self.canvas,
                        int(self.x1Entry.get()),
                        int(self.y1Entry.get()),
                        int(self.x2Entry.get()),
                        int(self.y2Entry.get()),
                        fill="white")
        except:
            tkMessageBox.showerror("Item", "Cannot create new item")

    def LiftObj(self):
        if (self.canvas == None):
            global instance
            self.canvas = instance.canvas
        if (self.canvas and self.item and self.canvas.find_withtag(self.item)):
            self.canvas.lift(self.item)
        else:
            tkMessageBox.showerror("Item", "Item not found on canvas")

    def LowerObj(self):
        if (self.canvas == None):
            global instance
            self.canvas = instance.canvas
        if (self.canvas and self.item and self.canvas.find_withtag(self.item)):
            self.canvas.lower(self.item)
        else:
            tkMessageBox.showerror("Item", "Item not found on canvas")


class TagsTB:
    def __init__(self, master, app):
        self.app = app
        Label(master, text="Tag Manipulation",relief=RIDGE).grid(columnspan=4,sticky=NSEW,pady=4)
        Label(master, text="Reference").grid(row=1, columnspan=4)
        self.refTagEntry = Entry(master, bg="white")
        self.refTagEntry.grid(row=2, columnspan=4)
        Label(master, text="New").grid(row=3, columnspan=4)
        self.newTagEntry = Entry(master, bg="white")
        self.newTagEntry.grid(row=4, columnspan=4)
        Label(master, text="X1").grid(row=5, column=0)
        Label(master, text="Y1").grid(row=5, column=1)
        Label(master, text="X2").grid(row=5, column=2)
        Label(master, text="Y2").grid(row=5, column=3)
        self.x1Entry = Entry(master, bg="white", width=5)
        self.x1Entry.grid(row=6, column=0)
        self.y1Entry = Entry(master, bg="white", width=5)
        self.y1Entry.grid(row=6, column=1)
        self.x2Entry = Entry(master, bg="white", width=5)
        self.x2Entry.grid(row=6, column=2)
        self.y2Entry = Entry(master, bg="white", width=5)
        self.y2Entry.grid(row=6, column=3)

        Button(master, text="addtag_above",command=self.addAbove).grid(row=7, columnspan=4,sticky=EW)
        Button(master, text="addtag_all", command=self.addAll).grid(row=8, columnspan=4,sticky=EW)
        Button(master, text="addtag_below", command=self.addBelow).grid(row=9, columnspan=4,sticky=EW)
        Button(master, text="addtag_closest", command=self.addClosest).grid(row=10, columnspan=4,sticky=EW)
        Button(master, text="addtag_enclosed", command=self.addEnclosed).grid(row=11, columnspan=4,sticky=EW)
        Button(master, text="addtag_overlapping", command=self.addOverlap).grid(row=12, columnspan=4,sticky=EW)
        Button(master, text="addtag_withtag", command=self.addWithtag).grid(row=13, columnspan=4,sticky=EW)

    def addAbove(self):
        if (self.newTagEntry.get() != ""):
            self.app.canvas.addtag_above(self.newTagEntry.get(), self.refTagEntry.get())

    def addAll(self):
        if (self.newTagEntry.get() != ""):
            self.app.canvas.addtag_all(self.newTagEntry.get())

    def addBelow(self):
        if (self.newTagEntry.get() != ""):
            self.app.canvas.addtag_below(self.newTagEntry.get(), self.refTagEntry.get())

    def addClosest(self):
        self.app.canvas.addtag_closest(self.newTagEntry.get(),
                                       int(self.x1Entry.get()),
                                       int(self.y1Entry.get()))

    def addEnclosed(self):
        if (self.newTagEntry.get() != ""):
            self.app.canvas.addtag_enclosed(self.newTagEntry.get(),
                                            int(self.x1Entry.get()),
                                            int(self.y1Entry.get()),
                                            int(self.x2Entry.get()),
                                            int(self.y2Entry.get()))

    def addOverlap(self):
        if (self.newTagEntry.get() != ""):
            self.app.canvas.addtag_overlapping(self.newTagEntry.get(),
                                               int(self.x1Entry.get()),
                                               int(self.y1Entry.get()),
                                               int(self.x2Entry.get()),
                                               int(self.y2Entry.get()))

    def addWithtag(self):
        if (self.newTagEntry.get() != ""):
            self.app.canvas.addtag_withtag(self.newTagEntry.get(),
                                           self.refTagEntry.get())

root = Tk()
root.title("Tkinter tags demo")
itemTL = Toplevel(root)
itemTL.title("Item manipulation")
itemTL.transient(root)
item_tb = ItemTB(itemTL)

instance = App(root, item_tb)

findTL = Toplevel(root)
findTL.title("Search")
findTL.transient(root)
find_tb = FindTB(findTL, instance)

tagTL = Toplevel(root)
tagTL.title("Tag manipulation")
tagTL.transient(root)
tag_tb = TagsTB(tagTL, instance)

root.mainloop()