from Tkinter import *

class AllTkinterWidgets:
      def __init__(self, master):
        frame = Frame(master, width=500, height=400)
        frame.pack(expand = 0)

        # ---------------------Menu Creation ------------------------
        self.mbar = Frame(frame, relief = 'raised', width=500, bd = 2)
        self.mbar.pack(expand = 0, fill = X, side = TOP)

        # Create File menu ------------------------------------------
        self.filebutton = Menubutton(self.mbar, text = 'File')
        self.filebutton.pack(side = LEFT)
        self.filemenu = Menu(self.filebutton, tearoff=0)
        self.filebutton['menu'] = self.filemenu

        # Populate File menu
        self.filemenu.add('command', label = 'Exit', command = root.quit)

        # Create forground menu ------------------------------------------
        self.fgbutton = Menubutton(self.mbar, text = 'Foreground')
        self.fgbutton.pack(side = LEFT)
        self.fgmenu = Menu(self.fgbutton, tearoff=0)
        self.fgbutton['menu'] = self.fgmenu

        # Populate Forground menu
        self.fgmenu.add('command', label = 'Red', command = self.fgred)
        self.fgmenu.add('command', label = 'Black', command = self.fgblack)
        self.fgmenu.add('command', label = 'White', command = self.fgwhite)

        # Create background menu ------------------------------------------
        self.bgbutton = Menubutton(self.mbar, text = 'Background')
        self.bgbutton.pack(side = LEFT)
        self.bgmenu = Menu(self.bgbutton, tearoff=0)
        self.bgbutton['menu'] = self.bgmenu

        # Populate background menu
        self.bgmenu.add('command', label = 'Green', command = self.bggreen)
        self.bgmenu.add('command', label = 'Black', command = self.bgblack)
        self.bgmenu.add('command', label = 'White', command = self.bgwhite)

        # Create size menu ------------------------------------------
        self.szbutton = Menubutton(self.mbar, text = 'Size')
        self.szbutton.pack(side = LEFT)
        self.szmenu = Menu(self.szbutton, tearoff=0)
        self.szbutton['menu'] = self.szmenu

        # Populate size menu
        self.szmenu.add('command', label = 'Font 8', command = self.size8)
        self.szmenu.add('command', label = 'Font 10', command = self.size10)
        self.szmenu.add('command', label = 'Font 12', command = self.size12)

        # Create Help menu ------------------------------------------
        self.helpbutton = Menubutton(self.mbar, text = 'Help')
        self.helpbutton.pack(side = RIGHT)
        self.helpmenu = Menu(self.helpbutton, tearoff=0)
        self.helpbutton['menu'] = self.helpmenu

        # Populate Help menu
        self.helpmenu.add('command', label = 'About', command = self.about)

        # ----------------- RadioButtonBar Creation ----------------
        self.rbbar = Frame(frame, relief = 'sunken', width=500, bd = 2)
        self.rbbar.pack(expand = 1, fill = BOTH, side = BOTTOM, pady = 5)

        # CHANGE HERE
        self.v = StringVar()
        Label(self.rbbar, text='Font Name:').pack(side=LEFT, padx=5)
        self.rCourier  = Radiobutton(self.rbbar, text='Courier', variable = self.v, value='Courier', command=self.OnCourier)
        self.rTimes    = Radiobutton(self.rbbar, text='Times', variable = self.v, value='Times', command=self.OnTimes)
        self.rHelvetic = Radiobutton(self.rbbar, text = 'Helvetic', variable = self.v, value='Helvetic', command=self.OnHelvetic)

        self.rCourier.pack(side=LEFT)
        self.rTimes.pack(side=LEFT)
        self.rHelvetic.pack(side=LEFT)
        self.rCourier.select()

        # ------------------- ButtonBar Creation --------------------
        self.bbar = Frame(frame, relief = 'sunken', width=500, bd = 2)
        self.bbar.pack(expand = 1, fill = BOTH, side = BOTTOM, pady = 5, before = self.rbbar)

        self.vcb1 = StringVar()
        self.vcb2 = StringVar()
        self.vcb3 = StringVar()
        Label(self.bbar, text='Font Type:').pack(side=LEFT, padx=5)
        self.cbBold = Checkbutton(self.bbar, text='Bold', variable = self.vcb1, onvalue='bold', offvalue='', command=self.OnBold)
        self.cbBold.pack(side=LEFT, padx=5)
        self.cbItalic = Checkbutton(self.bbar, text='Italic', variable = self.vcb2, onvalue='italic', offvalue='', command=self.OnItalic)
        self.cbItalic.pack(side=LEFT, padx=5)
        self.cbUndln = Checkbutton(self.bbar, text='Underlined', variable = self.vcb3, onvalue='underline', offvalue='', command=self.OnUnderline)
        self.cbUndln.pack(side=LEFT, padx=5)

        self.sc = Scale(self.bbar, from_=8.0, to=16.0, label='Font Size', orient=HORIZONTAL)
        self.sc.set(10)
        self.sc.pack(expand = 0, side=RIGHT, fill = NONE)
        self.sc.bind("<ButtonRelease-1>", self.size)

        # -------------------- entry box frame ---------------------
        self.t = StringVar()
        self.ef = Frame(frame, bd=2, relief='groove')
        self.lb2 = Label(self.ef, text='File:')
        self.lb2.pack(side= LEFT)
        self.entry = Entry(self.ef, textvariable = self.t, bg='white')
        self.bt = Button(self.ef, text = 'Load..', command = self.load)
        self.entry.pack(side = LEFT, padx = 5)
        self.bt.pack(side = LEFT, padx= 5)
        self.ef.pack(expand=0, fill=X, pady=5, before = self.bbar, side = BOTTOM)

        #--------------------- listbox frame ------------------------
        self.lf = Frame(frame, bd=2, relief='groove')
        self.lb = Label(self.lf, text='Past Events:')
        self.bt1 = Button(self.lf, text = 'Clear', command = self.clear)
        self.listbox = Listbox(self.lf, height=4)
        self.sbl = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.sbl.set)
        self.lb.pack(side=LEFT, padx=5)
        self.bt1.pack(side = BOTTOM)
        self.sbl.pack(side=RIGHT, fill=Y)
        self.listbox.pack(padx=5, fill = X)
        self.lf.pack(expand=0, fill=X, pady=5, before = self.ef, side = BOTTOM)

        #------------------- text editor frame -----------------------
        self.tf = Frame(frame, bd=2, relief=SUNKEN)
        self.text = Text(self.tf, height=10, width =65, wrap = WORD)
        self.text.pack(side=LEFT,padx=5, expand =0)
        self.sb = Scrollbar(self.tf, orient=VERTICAL, command=self.text.yview)
        self.sb.pack(side=RIGHT, fill=Y)
        self.text.configure(yscrollcommand=self.sb.set)
        self.text.configure(font = ('Courier', 10, 'normal'))
        self.tf.pack(expand=0, fill=BOTH, pady=10, padx=5, side = BOTTOM, before = self.lf)


      # -------------------- Function defs ------------------------
      def about(self):
          print "hello!"

      def clear(self):
          self.listbox.delete(0, END)

      def load(self):
          try:
             fd = open(self.t.get())
          except:
             self.listbox.insert(END, 'Error loading file ' + self.t.get())
          lines = fd.read()
          fd.close()
          self.text.insert(END, lines)
          self.listbox.insert(END, 'Loaded file ' + self.t.get())

      def size8(self):
          self.sc.set(8)
          self.size(NONE)

      def size10(self):
          self.sc.set(10)
          self.size(NONE)

      def size12(self):
          self.sc.set(12)
          self.size(NONE)

      def size(self, event):
          self.listbox.insert(END, 'Re-setting font size')
          self.Action()

      def OnCourier(self):
          self.listbox.insert(END, 'font family set to Courier')
          self.Action()

      def OnTimes(self):
          self.listbox.insert(END, 'font family set to Times')
          self.Action()

      def OnHelvetic(self):
          self.listbox.insert(END, 'font family set to Helvetic')
          self.Action()

      def OnBold(self):
          if (self.vcb1.get()):
             self.listbox.insert(END, 'font weight set to bold')
          else:
             self.listbox.insert(END, 'font weight set to normal')
          self.Action()

      def OnItalic(self):
          if (self.vcb2.get()):
             self.listbox.insert(END, 'font weight set to italic')
          else:
             self.listbox.insert(END, 'font weight set to normal')
          self.Action()

      def OnUnderline(self):
          if (self.vcb3.get()):
             self.listbox.insert(END, 'font weight set to underline')
          else:
             self.listbox.insert(END, 'font weight set to normal')
          self.Action()

      def Action(self, event=None):
          font_mod = ""
          font_mods = [self.vcb1.get(), self.vcb2.get(), self.vcb3.get()]
          for fm in font_mods:
              if (fm):
                  font_mod = "%s %s" % (font_mod, fm)
          if (font_mod == ""):
             font_mod = "normal"
          self.text.configure(font=(self.v.get(), self.sc.get(), font_mod))

      def fgred(self):
          self.listbox.insert(END, 'foreground color set to red ')
          self.text.configure(foreground = 'RED')

      def fgwhite(self):
          self.listbox.insert(END, 'foreground color set to white ')
          self.text.configure(foreground = 'WHITE')

      def fgblack(self):
          self.listbox.insert(END, 'foreground color set to black ')
          self.text.configure(foreground = 'BLACK')

      def bggreen(self):
          self.listbox.insert(END, 'background color set to green')
          self.text.configure(background = 'GREEN')

      def bgwhite(self):
          self.listbox.insert(END, 'background color set to white')
          self.text.configure(background = 'WHITE')

      def bgblack(self):
          self.listbox.insert(END, 'background color set to black')
          self.text.configure(background = 'BLACK')

# display the menu
root = Tk()
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.pack_propagate(0)
root.mainloop()







