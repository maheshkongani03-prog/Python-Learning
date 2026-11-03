from tkinter import * 
window=Tk()
window.title("GUI Design")
window.minsize(width=500, height=500)
my_label=Label(text="I am Label",font=('Aerial',24,'bold'))
my_label.pack()

my_label["text"]="enter an angel name"
my_label.config(text="enter an erripok name")








def button_clicked():
    new_text=input.get().lower()
    if new_text=="arhant":
        my_label.config(text=f"yes..!{new_text} is ERRIPOOKu!!!")
    else:
        my_label.config(text=f"No..!{new_text} is not an ERRIPOOKU!!!")







my_button=Button(text="Click Me",command=button_clicked)
my_button.pack()



input=Entry(width=20)
input.pack()








window.mainloop()