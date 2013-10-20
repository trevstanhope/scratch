from Tkinter import *

root = Tk()

root.title('Place geometry manager demo')
btn_count = 1
relx = 0.0
for i in range(5):
	Button(root, text='B%d' % btn_count).place(relx = relx, rely=0.2)
	relx= relx + 0.2
	btn_count = btn_count + 1

xpos = 10
for i in range(5):
	Button(root, text='B%d' %btn_count).place(x=xpos, y=150, relwidth=0.1, relheight=0.1)
	xpos = xpos + 40
	btn_count = btn_count + 1

Button(root, text="Corner").place(relx=0.9, rely=0.9, anchor=SE, relwidth = 0.2, relheight=0.2)
Button(root, text="Fixed").place(x=150, y = 100, width = 50, height=40)


mainloop()