from tkinter import *

root = Tk() #Line always first whenever working with tkinter

# Creating a Label Widget
myLabel = Label(root, text="Hello World!")

# Shoving it onto the screen
myLabel.pack()

root.mainloop()
