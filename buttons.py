from tkinter import *

root = Tk()  # Line always first whenever working with tkinter


def myClick():
    myLabel1 = Label(root, text="Look! I clicked a Button!!")
    myLabel1.pack()


myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()
