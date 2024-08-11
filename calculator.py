# CREATED BY <PRIYANSHUL SHARMA>
# Webpage Priyanshul.is-a.dev

from tkinter import *
from tkinter.ttk import *


window=Tk()
window.geometry("500x500")
window.title("calculater")


title=Label(window,text = "BASIC CALCULATER")
caption1=Label(window,text = "first value-")


caption2=Label(window,text = "second value-")

entry1=Entry(window)
entry2=Entry(window)

res=Label(window,text= "result")
result=Label(window)


title.grid(row=0,column=1,columnspan=3,pady=50)
caption1.grid(row=1,column=0,padx=25)
caption2.grid(row=2,column=0)


entry1.grid(row=1,column=2)
entry2.grid(row=2,column=2)


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


add=Button(window,text="add",command=add)
sub=Button(window,text="sub",command=sub)
mul=Button(window,text="multiply",command=mul)
div=Button(window,text="divide",command=div)


add.grid(row=1,column=4,padx=30)
sub.grid(row=2,column=4,padx=30)
mul.grid(row=3,column=4,padx=30)
div.grid(row=4,column=4,padx=30)

window.mainloop()
