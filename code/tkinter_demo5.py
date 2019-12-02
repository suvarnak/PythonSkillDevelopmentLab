# to create a simple window

import tkinter
from tkinter.ttk import *
window = tkinter.Tk()
window.title("My first app")
window.geometry('600x400')

combo = Combobox(window)
combo['values'] = (2016,2017,2018,2019)
combo.current(2)
combo.grid(column=0,row=0)
window.mainloop()