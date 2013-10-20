from Tkinter import *

pack_cmds = { "t" : TOP,
              "b" : BOTTOM,
              "l" : LEFT,
              "r" : RIGHT }

cmd_help = [ "t: pack at the top",
             "b: pack at the bottom",
             "l: pack at the left",
             "r: pack at the right",
             "",
             "xy: fill = BOTH",
             "x: fill = X",
             "y: fill = Y",
             "",
             "e: expand = YES",
             "",
             "q: quit creation loop" ]

print "Tkinter packer demo"
print "-"*19
for str in cmd_help:
    print str
print "-"*19

root = Tk()
frm1 = Frame(root, background="white")
frm1.pack(expand=YES, fill=BOTH)

loop_cond = 1
btn_count = 1
while (loop_cond):
    print "Enter a command: "
    s = raw_input()

    if (s == "q"):
        loop_cond = 0
    else:
        if (s.find("xy") >= 0):
           pack_fill = BOTH
        elif ("x" in s):
           pack_fill = X
        elif ("y" in s):
           pack_fill = Y
        else:
           pack_fill = NONE

        pack_exp = "e" in s

        for c in s:
           if (pack_cmds.get(c, "")):
               pack_side = pack_cmds[c]
               btn_text = "B%d - %s" % (btn_count, pack_side)
               Button(frm1, text=btn_text).pack(side=pack_side,
                                                expand = pack_exp,
                                                fill = pack_fill)
               btn_count = btn_count + 1

print "entering main loop"
root.mainloop()
