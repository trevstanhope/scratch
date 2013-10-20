# Line tool demo -- Tkinter
# Bruno Dufour May 10 2001
# File: test2.py

from Tkinter import *

class App:
	# Global identifiers for Application Status
	__AS_CREATE = 1
	__AS_MOVE = 2
	__AS_RESIZE = 3

	# Global identifiers for Dragging Status
	__DS_NODRAG = 1
	__DS_DRAGGING = 2

	# Initialization
	def __init__(self, master):
		self.dragmode = self.__DS_NODRAG
		# Radio buttons require a variable of a Tkinter-defined
		# type in order to store the value of the selected item
		self.app_status = IntVar(master)

		self.canvas = Canvas(master, bg="white") # Create canvas
		self.toolbar = Frame(master)             # Create Toolbar

		# Create Radio Buttons for status selection
		self.RadioCreate = Radiobutton(self.toolbar,
					       text="Create",
					       variable=self.app_status,
					       value = self.__AS_CREATE)
		self.RadioMove = Radiobutton(self.toolbar,
					     text="Move",
					     variable=self.app_status,
					     value = self.__AS_MOVE)
		self.RadioResize = Radiobutton(self.toolbar,
		                               text="Resize",
		                               variable=self.app_status,
		                               value = self.__AS_RESIZE)

		# Pack all radio buttons in toolbar
		self.RadioCreate.pack(side=LEFT, padx=2, pady=2)
		self.RadioMove.pack(side=LEFT, padx=2, pady=2)
		self.RadioResize.pack(side=LEFT, padx=2, pady=2)
		# Initialize the status to __AS_CREATE
		self.RadioCreate.select()

		# Pack the toolbar at the top
		self.toolbar.pack(side=TOP, fill=X)
		# Bind mouse events to canvas
		self.canvas.bind("<Button-1>", self.OnCanvasClicked)
		self.canvas.bind("<B1-Motion>", self.OnCanvasMouseDrag)
		self.canvas.bind("<ButtonRelease-1>", self.OnCanvasMouseUp)
		self.canvas.bind("<Button-3>", self.OnCanvasB3Clicked)
		# Pack the canvas at the bottom, making it expand to fill
		# the entire client area of the window
		self.canvas.config(closeenough=2.0)
		self.canvas.pack(side=BOTTOM, fill=BOTH,expand=1)

	# Canvas Mouse events
	# ------------------------------------------------------------------------------------------
	def OnCanvasClicked(self,event):
		# get the current status of the application. Since it is an IntVar
		# get() must be called to obtain its value.
		current_status = self.app_status.get()

		if (current_status == self.__AS_CREATE):
			if (self.dragmode == self.__DS_NODRAG):
				self.dragmode = self.__DS_DRAGGING
				self.OrgX = event.x
				self.OrgY = event.y
				self.CurrLine = self.canvas.create_line(event.x, event.y, event.x, event.y, fill="red")
		elif (current_status == self.__AS_MOVE):
			if (self.dragmode == self.__DS_NODRAG and self.canvas.find_withtag(CURRENT)):
				self.dragmode = self.__DS_DRAGGING
				self.OrgX = event.x
				self.OrgY = event.y
				self.CurrLine = CURRENT
		else:
			if (self.dragmode == self.__DS_NODRAG and self.canvas.find_withtag(CURRENT)):
				self.dragmode = self.__DS_DRAGGING
				self.CurrLine = CURRENT
				line_coords = self.canvas.coords(CURRENT)
				line_center_x = (line_coords[2] + line_coords[0]) / 2
				if (line_coords[2] > line_coords[0]):
					if (event.x >= line_center_x):
						self.OrgX = line_coords[0]
						self.OrgY = line_coords[1]
					else:
						self.OrgX = line_coords[2]
						self.OrgY = line_coords[3]
				else:
					if (event.x >= line_center_x):
						self.OrgX = line_coords[2]
						self.OrgY = line_coords[3]
					else:
						self.OrgX = line_coords[0]
						self.OrgY = line_coords[1]
				self.canvas.coords(self.CurrLine, self.OrgX, self.OrgY, event.x, event.y)


	def OnCanvasMouseUp(self,event):
		if (self.canvas.find_withtag(CURRENT)):
			self.canvas.itemconfig(CURRENT, fill="black")
		if (self.dragmode == self.__DS_DRAGGING):
			self.dragmode = self.__DS_NODRAG
			self.canvas.itemconfig(self.CurrLine, fill="black")
			if (self.app_status.get() == self.__AS_CREATE):
				self.canvas.tag_bind(self.CurrLine, "<Enter>", self.OnLineMouseEnter)
				self.canvas.tag_bind(self.CurrLine, "<Leave>", self.OnLineMouseLeave)

	def OnCanvasMouseDrag(self,event):
		if (self.dragmode == self.__DS_DRAGGING):
			current_status = self.app_status.get()
			if (current_status == self.__AS_CREATE):
				self.canvas.coords(self.CurrLine, self.OrgX, self.OrgY, event.x, event.y)
			elif (current_status == self.__AS_MOVE and self.canvas.find_withtag(CURRENT)):
				dx = event.x - self.OrgX
				dy = event.y - self.OrgY
				self.canvas.move(self.CurrLine, dx, dy);
				self.OrgX = event.x
				self.OrgY = event.y
			else:
				self.canvas.coords(self.CurrLine, self.OrgX, self.OrgY, event.x, event.y)

	def OnCanvasB3Clicked(self,event):
		if (self.dragmode == self.__DS_DRAGGING):
			self.canvas.delete(self.CurrLine)

	def OnLineMouseEnter(self,event):
		current_status = self.app_status.get()
		if (current_status == self.__AS_MOVE):
			self.canvas.itemconfig(CURRENT, fill="blue")
		elif (current_status == self.__AS_RESIZE):
			self.canvas.itemconfig(CURRENT, fill="green")

	def OnLineMouseLeave(self, event):
		if (self.dragmode != self.__DS_DRAGGING):
			if(self.canvas.find_withtag(CURRENT)):
				self.canvas.itemconfig(CURRENT, fill="black")

	# ------------------------------------------------------------------------------------------

root = Tk()

root.title("Line tool -- Tkinter canvas")

app = App(root)

root.mainloop()
