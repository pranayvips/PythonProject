from tkinter import *
from functools import partial

root = Tk()
root.geometry('700x500')

def abc(name,age):
    pass

people = []
def load():
    Button(root,text="back",command=lambda:unload()).place(x=200,y=200)
    people.clear()
    for i in range(90):
        for j in range(6):
            people.append(Label(root,text=str(i)+str(j)))
            people[-1].grid(row=i,column=j)
def unload():
    for i in people:
        i.grid_forget()
load()



root.mainloop()