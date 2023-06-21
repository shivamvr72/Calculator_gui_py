#============imported stuff======
from tkinter import*
import math
from tkinter import messagebox
#=========window==============
root = Tk()
root.geometry("381x219+750+150")
root.title("Calculator")
root.resizable(0,0)

#===========display==========
de = StringVar()
ent = Entry(root,  width=26,textvariable=de,bd=3, justify=RIGHT, font="mosserate 19 bold")
ent.grid(row=0, columnspan=5, pady=7, padx=4)

#========functions==============
def eqaulto(event=None):
    try:
        de.set(eval(f"{de.get()}"))
    except:
        messagebox.showerror("Invalid!", "Invalid Opeation!")

def sq():
    # de.set(int(f"{de.get()}"))
    # for i in range(de/2):
    #     i = de**2
    #     de.get("")
    try:
        xo = de.get()
        x=math.sqrt(int(xo))
        de.set(f"{x}")
    except:
        messagebox.showerror("Invalid!", "Invalid Opearation!")


def pr(event=None):
    try:
        int(de.get())
        de.set(int(f"{de.get()*0.01}*"))
    except ValueError:
        op = ["*","+","-"]
        for i in op:
            if (i in de.get()):
                x=int(float(de.get().split(i)[0]))
                y=int(float(de.get().split(i)[1]))
                if (i == "*"):
                    de.set(f"{x*0.01*y}")
                elif (i == "+"):
                    de.set(f"{x+(x*0.01*y)}")
                elif (i == "-"):
                    de.set(f"{x-(x*0.01*y)}")
                else:
                    messagebox.showerror("Invalid","Invalid Operation!")

    # try:
    #     de.set(int(f"{de.get()*0.01}*"))
    # except:
    #     try:
    #         x=int(float(de.get().split("*")[0]))
    #         y=int(float(de.get().split("*")[1]))
    #         de.set(f"{x*0.01*y}")
    #     except:
    #         try:
    #             x=int(float(de.get().split("+")[0]))
    #             y=int(float(de.get().split("+")[1]))
    #             de.set(f"{(x*0.01*y)+x}")
    #         except:
    #             try:
    #                 x=int(float(de.get().split("-")[0]))
    #                 y=int(float(de.get().split("-")[1]))
    #                 de.set(f"{x-(x*0.01*y)}")
    #             except:
    #                 messagebox.showerror("invalid", "Invalid Operation!")

def bsp():
    de.set(f"{de.get()[:-1]}")


#===========colors============
clrsbg = "#febebe"
clrsfg = "#fefefe"
root.config(bg=clrsbg)

label = Label(root, text="powered by python", bg=clrsbg, fg="#000", font='moserrate 6 bold').grid(row=1, column=4, columnspan=5)
#============buttons============
b1 = Button(root, text="1", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}1")).grid(row=4, column=0, pady=3)
b2 = Button(root, text="2", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}2")).grid(row=4, column=1)
b3 = Button(root, text="3", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}3")).grid(row=4, column=2)

b4 = Button(root, text="4", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}4")).grid(row=3, column=0)
b5 = Button(root, text="5", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}5")).grid(row=3, column=1)
b6 = Button(root, text="6", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}6")).grid(row=3, column=2)

b7 = Button(root, text="7", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}7")).grid(row=2, column=0, pady=3)
b8 = Button(root, text="8", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}8")).grid(row=2, column=1)
b9 = Button(root, text="9", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}9")).grid(row=2, column=2)

b0 = Button(root, text="0", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}0")).grid(row=5, column=0)
bd = Button(root, text=".", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}.")).grid(row=5, column=1)
be = Button(root, text="=", font="moserrate 12 bold", width=4, command=eqaulto).grid(row=5, column=2)

ba = Button(root, text="+", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}+")).grid(row=5, column=3)
bs = Button(root, text="-", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}-")).grid(row=4, column=3)
bm = Button(root, text="x", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}*")).grid(row=3, column=3)
bd = Button(root, text="/", font="moserrate 12 bold", width=4, command=lambda:de.set(f"{de.get()}/")).grid(row=2, column=3)

bc = Button(root, text="CE", font="moserrate 12 bold", width=4, command=lambda:de.set("")).grid(row=5, column=4)
bx = Button(root, text="%", font="moserrate 12 bold", width=4, command=pr).grid(row=4, column=4)
br = Button(root, text="R", font="moserrate 12 bold", width=4, command=sq).grid(row=3, column=4)
bb = Button(root, text="<x", font="moserrate 12 bold", width=4, command=bsp).grid(row=2, column=4)

#================Button Binding==============
root.bind("0", lambda event=None:de.set(f"{de.get()}0"))
root.bind("1", lambda event=None:de.set(f"{de.get()}1"))
root.bind("2", lambda event=None:de.set(f"{de.get()}2"))
root.bind("3", lambda event=None:de.set(f"{de.get()}3"))
root.bind("4", lambda event=None:de.set(f"{de.get()}4"))
root.bind("5", lambda event=None:de.set(f"{de.get()}5"))
root.bind("6", lambda event=None:de.set(f"{de.get()}6"))
root.bind("7", lambda event=None:de.set(f"{de.get()}7"))
root.bind("8", lambda event=None:de.set(f"{de.get()}8"))
root.bind("9", lambda event=None:de.set(f"{de.get()}9"))
root.bind("+", lambda event=None:de.set(f"{de.get()}+"))
root.bind("-", lambda event=None:de.set(f"{de.get()}-"))
root.bind("*", lambda event=None:de.set(f"{de.get()}*"))
root.bind("/", lambda event=None:de.set(f"{de.get()}/"))
root.bind(".", lambda event=None:de.set(f"{de.get()}."))
#root.bind("", lambda event=None:de.set(f"{de.get()}"))

root.bind("<Return>",eqaulto)
root.bind("<BackSpace>", lambda event=None:de.set(f"{de.get()[:-1]}"))
root.bind("<Button-1>", lambda event=None:root.focus_force())

#===========mainloop for window================
root.mainloop()