# GUI with Tkinter

from tkinter import *  # basically import everything


def btnClick():
    myLabel1 = Label(root, text="btn Changed").grid(row=0,column=0)

root = Tk()  #basically the start of every tkinter or main method
#creating label widgets
myLabel1 = Label(root, text="Hello World").grid(row=0, column=0) #label widget
myLabel2 = Label(root, text="My name is Justin Santos").grid(row=1, column=5) #label widget
myButton = Button(root, text='Button', padx=50, pady=50, command=btnClick).grid(row = 3,column=0) # enable or siable it with state
# myLabel.pack() #Showing it to Screen
# myLabel1.grid(row=0, column=0)   #Grid System
# myLabel2.grid(row=1, column=5)  # this won't work because its relative to the method before it




root.mainloop()# basically loop infinitely aslong as the program runs

