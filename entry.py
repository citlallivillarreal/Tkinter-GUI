from tkinter import *

root = Tk()  # Line always first whenever working with tkinter

e = Entry(root, width=50)
e.pack()
e.get()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel1 = Label(root, text=hello)
    myLabel1.pack()


myButton = Button(root, text="Enter Your Name", command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()
