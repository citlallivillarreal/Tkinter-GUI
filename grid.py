from tkinter import *

root = Tk() #Line always first whenever working with tkinter

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Lali")

# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()
