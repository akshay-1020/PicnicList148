from tkinter import *
import random

root = Tk()
root.title("Random Number List")
root.geometry("400x400")

itemlist = Label(root)
displaynum = Label(root)
bag = ["apple", "mat", "basket", "bottle", "cap"]
itemlist["text"] = str(bag)

def pickitem():
    r = random.randint(0,4)
    displaynum["text"] = "Put " + str(bag[r]) + " in your bag."

btn=Button(root,text="What should I put in my bag?",command=pickitem)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

itemlist.place(relx=0.5,rely=0.4,anchor=CENTER)
displaynum.place(relx=0.5,rely=0.5,anchor=CENTER)
    
root.mainloop()