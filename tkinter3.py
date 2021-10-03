from tkinter import *

def function1():
    num1 = float(el1.get())
    num2 = float(el2.get())

    result = num1 + num2
    el3.delete(0, END)
    el3.insert(0, result)

root = Tk()
Label(root, text="+").grid(row=0, column=1)
el1 = Entry(root)
el2 = Entry(root)
el3 = Entry(root)
el1.grid(row=0, column=0)
el2.grid(row=0, column=2)
el3.grid(row=0, column=4)
Button(root, text="=", command=function1).grid(row=0, column=3)
root.mainloop()