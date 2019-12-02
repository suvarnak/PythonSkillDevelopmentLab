# to create a simple window

import tkinter

window = tkinter.Tk()
window.title("My first app")
window.geometry('600x400')
username_label = tkinter.Label(master=window,foreground="red",background="yellow",text="User Name")

#grid is a geometry manager organizes widgets in a table-like structure in the parent widget.
username_label.grid(column=0,row=0)

password_label = tkinter.Label(master=window,foreground="red",background="yellow",text="Password")
password_label.grid(column=0,row=1)

window.mainloop()