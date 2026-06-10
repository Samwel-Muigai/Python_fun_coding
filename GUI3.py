from tkinter import *

w = Tk()

w.geometry("650x780")
w.configure(background="beige")
w.title("Example of GUI")

var=StringVar()

def multiply():
    a=int(E1.get())
    b=int(E2.get())
    c=int(E3.get())
    d=int(a*b*c)

    var.set(d)

L1=Label(w, text="Number One", bg="beige")
L2=Label(w, text="Number Two", bg="beige")
L3=Label(w, text="Number Three", bg="beige")
L4=Label(w, text="Result", bg="beige")

L1.grid(row=0, sticky=W)
L2.grid(row=1, sticky=W)
L3.grid(row=2, sticky=W)
L4.grid(row=3, sticky=W)

E1=Entry(w)
E2=Entry(w)
E3=Entry(w)
E4=Entry(w, textvariable=var)

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)
E4.grid(row=3, column=1)

B1=Button(w, text="OK", bg="beige", command=multiply)
B1.grid(row=4, column=1)

w.mainloop()