from tkinter import *

window=Tk()
window.title("miles to km")
def clicked():
    inpu=float(miles.get())
    kms=inpu*1.6
    result.config(text=kms)
miles=Entry()
miles.grid(column=1,row=0)
miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)


is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)


result=Label(text="0")
result.grid(column=1,row=1)


kilometer=Label(text="Km")
kilometer.grid(column=2,row=1)


calculate_button=Button(text="calculate",command=clicked)
calculate_button.grid(column=1,row=2)

window.mainloop()