from Tkinter import *
from scrolledtext import ScrolledText
from time import ctime

global widgets

eventList = { "2" : "KeyPress",
              "3" : "KeyRelease",
              "4" : "ButtonPress",
              "5" : "ButtonRelease",
              "6" : "Motion",
              "7" : "Enter",
              "8" : "Leave",
              "9" : "FocusIn",
              "10": "FocusOut",
              "12": "Expose",
              "15": "Visibility",
              "17": "Destroy",
              "18": "Unmap",
              "19": "Map",
              "21": "Reparent",
              "22": "Configure",
              "24": "Gravity",
              "26": "Circulate",
              "28": "Property",
              "32": "Colormap",
              "36": "Activate",
              "37": "Deactivate" }

stdevents = [ "<Button-1>",  "<Button-2>",  "<Button-3>",
              "<B1-Motion>", "<B2-Motion>", "<B3-Motion>",
              "<ButtonRelease-1>", "<ButtonRelease-2>", "<ButtonRelease-3>",
              "<Double-Button-1>", "<Double-Button-2>", "<Double-Button-3>",
              "<Configure>",
              "<Control-Insert>", "<Control-Shift-F3>", "<Control-Alt-F>",
              "<Enter>", "<Leave>",
              "<Expose>",
              "<FocusIn>",
              "<FocusOut>",
              "<KeyPress>",
              "<KeyRelease-backslash>",
              "<Map>",
              "<Print>",
              "A", "Z" ]

class Toolbar(Frame):
    def __init__(self, parent=None, side=RIGHT):
        Frame.__init__(self, parent)
        if side in [RIGHT, LEFT]:
            Fill = Y
        else:
            Fill = X
        self.pack(side=side, fill=Fill)
        self.createWidgets()

    def createWidgets(self):
        Label(self, text="Events", relief=RIDGE).pack(fill=X, pady=2)

        eventListFrm = Frame(self)
        self.eventList = Listbox(eventListFrm, selectmode=EXTENDED)
        self.eventList.pack(side=LEFT, expand=YES, fill=Y)
        eventListScroll = Scrollbar(eventListFrm, command=self.eventList.yview)
        eventListScroll.pack(side=RIGHT, expand=YES, fill=Y)
        self.eventList.configure(yscrollcommand=eventListScroll.set)
        eventListFrm.pack(fill=X)

        Label(self, text="Event description:", relief=RIDGE).pack(fill=X, pady=2)
        self.eventEntry = Entry(self, bg="white")
        self.eventEntry.pack()
        self.eventEntry.bind("<KeyPress-Return>", self.OnEntryKeyReturn)
        self.bindEventButton = Button(self, text="Bind", command=self.btnAddClick)
        self.bindEventButton.pack(fill=X)
        self.unbindEventButton = Button(self, text="Unbind", command=self.btnDelClick)
        self.unbindEventButton.pack(fill=X)

        stdListFrm = Frame(self)
        self.stdList = Listbox(stdListFrm)
        self.stdList.pack(side=LEFT, expand=YES, fill=Y)
        stdListScroll = Scrollbar(stdListFrm, command=self.stdList.yview)
        stdListScroll.pack(side=RIGHT, expand=YES, fill=Y)
        self.stdList.configure(yscrollcommand=stdListScroll.set)

        for eventstr in stdevents:
            self.stdList.insert(END, eventstr)
        self.stdList.bind("<Double-1>", self.OnListDblClick)
        self.stdList.bind("<Button-1>", self.OnListClick)
        stdListFrm.pack(fill=X)

        self.MustBreak = IntVar(self)
        self.MustBreak.set(0)
        Checkbutton(self, variable=self.MustBreak, text="Break after event").pack(fill=X)

    def OnListClick(self, event):
        i = self.stdList.nearest(event.y)
        eventstr = self.stdList.get(i)
        if eventstr:
            self.eventEntry.delete(0, END)
            self.eventEntry.insert(0, eventstr)

    def OnListDblClick(self, event):
        i = self.stdList.nearest(event.y)
        if (i >= 0):
            self.addEvent(widgetlist=widgets, eventMTQ=self.stdList.get(i))

    def OnEntryKeyReturn(self, event):
    	self.btnAddClick()

    def btnAddClick(self):
        self.addEvent(widgetlist=widgets, eventMTQ=self.eventEntry.get())
        self.eventEntry.selection_range(0, END)

    def btnDelClick(self):
        while (self.eventList.curselection()):
            i = self.eventList.curselection()[0]
            self.delEvent(widgetlist=widgets, eventMTQ=self.eventList.get(i))
            self.eventList.delete(i)


    def addEvent(self, widgetlist=None, eventMTQ=""):
        if eventMTQ:
            try:
                for wgt in widgetlist:
                    wgt.bind(eventMTQ, self.reportEvent)
                self.eventList.insert(END, eventMTQ)
            except:
                print "Event %s not supported by widget %s" % (eventMTQ, str(wgt))

    def delEvent(self, widgetlist=None, eventMTQ=""):
        for wgt in widgetlist:
            wgt.unbind(eventMTQ)

    def reportEvent(self, event):
        global st
        rpt = "%s" % (45*"=")
        rpt = "%s\nEvent: type=%s (%s)" %  (rpt, event.type,
                                            eventList.get(event.type, "Unknown"))
        rpt = "%s\ntime=%s"   %            (rpt, event.time)
        rpt = "%s  widget=%s" %            (rpt, event.widget)
        rpt = "%s\nx=%d, y=%d"%            (rpt, event.x, event.y)
        rpt = "%s  x_root=%d, y_root=%d" % (rpt, event.x_root, event.y_root)
        rpt = "%s\nserial=%s" %            (rpt, event.serial)
        rpt = "%s  num=%s" %               (rpt, event.num)
        rpt = "%s  height=%s" %            (rpt, event.height)
        rpt = "%s  width=%s" %             (rpt, event.width)
        rpt = "%s\nkeysym=%s" %            (rpt, event.keysym)
        rpt = "%s  ksNum=%s" %         (rpt, event.keysym_num)

        #### some event types don"t have these attributes
        try:
            rpt = "%s  focus=%s" %   (rpt, event.focus)
        except:
            pass
        try:
            rpt = "%s  send=%s" %    (rpt, event.send_event)
        except:
            pass
        rpt = "%s\n\n" % rpt
        st.addText(rpt)
        st.see(END)
        print event.time
        if self.MustBreak.get():
            return "break"

root = Tk()
root.title("Tkinter events demo")

eventTB = Toolbar(root, side=RIGHT)
eventTB.pack()

frmTest = Frame(root)
frmTest.pack(expand=YES, fill=Y, side=LEFT)

st = ScrolledText(root, side=LEFT)

Label(frmTest, text="Test widgets", relief=RIDGE).pack(fill=X, pady=2)
Label(frmTest, text="\n").pack(fill=X)
ent = Entry(frmTest, bg="white", name="entry")
ent.pack(side=TOP, fill=X)
lbl = Label(frmTest, text="Test Label", relief=RIDGE, name="label")
lbl.pack(side=TOP, fill=X)
Button(frmTest, text="Clear Text", command=st.clear).pack(side=BOTTOM, fill=X)

widgets = (ent, lbl)

mainloop()