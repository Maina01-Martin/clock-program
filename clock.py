from tkinter import *
from time import *

def update():
    time_string =strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    time_label.after(1000,update)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)



window = Tk()

time_label =Label(window,font=("Arial",50),fg='black')
time_label.pack()

day_label =Label(window,font=("Arial",40))
day_label.pack()

date_label =Label(window,font=("Arial",40))
date_label.pack()


update()
window.mainloop()
