from tkinter import *

window=Tk()
window.title("converter")
num=""
my=Label(text="miles")
my.grid(column=2,row=1)

def button_clicked():
    use=float(inty.get())
    kilometer=use*1.6
    equal.config(text=f"is equal to     {kilometer}      km")
    equal.grid(row=2)
    
#input
inty=Entry(width=10)
inty.grid(row=1)

##miles

##is equal

equal=Label(text=f"is equal to           km")
equal.grid(row=2)

##button
button=Button(text="calculate",command=button_clicked)
button.grid(row=3)























window.mainloop()