from tkinter import *

w = Tk()

w.geometry("400x450")
w.configure(background="silver")
w.title("BMI Calculator")

var = StringVar()

def calculate():
    height = float(E1.get())
    weight = float(E2.get())

    height = height / 100

    BMI = weight / (height * height)

    var.set(round(BMI, 2))

def delete_height():
    E1.delete(0, END)

def delete_weight():
    E2.delete(0, END)


L1 = Label(w, text="Height (cm)", bg="silver")
L2 = Label(w, text="Weight (kg)", bg="silver")
L3 = Label(w, text="BMI", bg="silver")

L1.grid(row=0, sticky=W, padx=10, pady=10)
L2.grid(row=1, sticky=W, padx=10, pady=10)
L3.grid(row=2, sticky=W, padx=10, pady=10)

E1 = Entry(w)
E2 = Entry(w)
E3 = Entry(w, textvariable=var)

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)

Bdel1 = Button(w, text="DEL", bg="red", fg="white",
               command=delete_height)

Bdel2 = Button(w, text="DEL", bg="red", fg="white",
               command=delete_weight)

Bdel1.grid(row=0, column=2, padx=5)
Bdel2.grid(row=1, column=2, padx=5)

B1 = Button(w, text="CHECK", bg="white",
            command=calculate)

B1.grid(row=3, column=1, pady=20)

w.mainloop()
