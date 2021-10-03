# import tkinter
from tkinter import *

def hello():
    print("hello")

# root = tkinter.Tk()
root =Tk()
root.title("TITLE")
root.minsize(400, 400)
Label(root, text="First Name").grid(row=0, column=0)
Label(root, text="Last Name").grid(row=1, column=0)
Entry(root).grid(row=0, column=1)
Entry(root).grid(row=1, column=1)
Button(root, text="Submit").grid(row=2, column=0)
# label1 = tkinter.Label(root, text="Hello Everyoe!")
# label1.pack()
# label2 = tkinter.Label(root, text="Good")
# label2.pack()
# button1 = tkinter.Button(root, text="Click me!", command=hello)
# button1.pack()
root.mainloop()