
from tkinter import *
from tkinter.ttk import *

#create the window
window=Tk()
window.geometry("500x500")
window.title("calculater")

#label text for title
title=Label(window,text = "BASIC CALCULATER")

#label 1
caption1=Label(window,text = "first value-")

#label 2
caption2=Label(window,text = "second value-")

#CREATInG ENTRY BUTTON
entry1=Entry(window)
entry2=Entry(window)

#CEATEING RESULT BUTTON
res=Label(window,text= "result")
result=Label(window)

#place labels
title.grid(row=0,column=1,columnspan=3,pady=50)
caption1.grid(row=1,column=0,padx=25)
caption2.grid(row=2,column=0)

#ENTRY PLACE
entry1.grid(row=1,column=2)
entry2.grid(row=2,column=2)

#RESULT BUTTON
res.grid(row=3,column=1)
result.grid(row=3,column=2)

def add():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result.configure(text=num1+num2)

def sub():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result.configure(text=num1-num2)

def mul():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result.configure(text=num1*num2)

def div():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result.configure(text=num1/num2)

#button
add=Button(window,text="add",command=add)
sub=Button(window,text="sub",command=sub)
mul=Button(window,text="multiply",command=mul)
div=Button(window,text="divide",command=div)

#place radiobutton and combobox
add.grid(row=1,column=4,padx=30)
sub.grid(row=2,column=4,padx=30)
mul.grid(row=3,column=4,padx=30)
div.grid(row=4,column=4,padx=30)

#calling main loop
window.mainloop()
