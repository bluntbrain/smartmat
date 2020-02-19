from tkinter import *


root = Tk()
root.minsize(600,600)

f = Frame(root,bg="grey",width=600,height=600)
f.grid(row=0,column=0,sticky="NW")
f.grid_propagate(0)
f.update()


weight = input()
# take serial weight input here
yogesh_weight = int(90)
chetan_weight = int(86)
name = "New user"

if(int(weight) == int(yogesh_weight)):
    name = "Yogesh"
elif(int(weight) == int(chetan_weight)):
    name = "Chetan"

w = Label(root, text="Hi "+ str(name) +"! How are You Doing Today!")
w.place(x=300, y=300, anchor="center")

w1 = Label(root, text="weight = " + str(weight) +" kgs")
w1.place(x=300, y=330, anchor="center")


#push data to cloud here like timestamp, weight, name, 
w2 = Label(root, text="data pushed to cloud")
w2.place(x=300, y=360, anchor="center")

# w.pack()
# w1.pack()
# w2.pack()


root.mainloop()
