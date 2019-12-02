# to create a simple window

import tkinter

window = tkinter.Tk()
window.title("My first app")
window.geometry('600x400')
username_label = tkinter.Label(master=window,foreground="red",background="yellow",text="User Name")
username_label.grid(column=0,row=0)
def submit_clicked():
	username_label.configure(text='changed')
submit_button = tkinter.Button(master=window,text='submit',command=submit_clicked)
submit_button.grid(column=0,row=1)
window.mainloop()