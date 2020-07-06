from tkinter import *

top = Tk()

top.geometry("1000x1000")
b = Button(top,text="Button")
b.pack()

checkButton = Checkbutton(top,text="Hello World")
checkButton.pack()

top.mainloop()