import tkinter
from tkinter import *
import math
from math import *


root= Tk()
root.title("sc calc")
root.resizable(False, False)
root.geometry("510x450")
root.configure(bg='dark red',pady="30")



equation = ""

    

def show(value):
    global equation
    equation+=value
    labell.config(text=equation)



def clear():
    global equation
    equation = ""
    labell.config(text=equation)

def calculate():
    global equation
    answer = ""
    if equation != "":
        try :
            answer = eval(equation)
        except:
            answer = "error"
            equation=""
    labell.config(text=answer)

    

labell = Label(root, width=15, height=3, text="", fg= "black", font=("Tahoma", 15, "bold"), bg="yellow")
labell.pack()
    






btn__0 = Button(root, text="0", width= 7, height= 2,  bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("0")).place(x=10, y=100)

btn__1 = Button(root, text="1", width= 7, height= 2, bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("1")).place(x=110, y =100)

btn__2 = Button(root, text="2", width= 7, height= 2, bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("2")).place(x=210, y =100)

btn__3 = Button(root, text="3", width= 7, height= 2,  bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("3")).place(x=310, y =100)

btn__4 = Button(root, text="4",width= 7, height= 2,  bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("4")).place(x=410, y =100)

btn__5 = Button(root, text="5", width= 7, height= 2,  bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("5")).place(x=10, y =150)

btn__6 = Button(root, text="6", width= 7, height= 2, bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("6")).place(x=110, y =150)

btn__7 = Button(root, text="7", width= 7, height= 2, bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("7")).place(x=210, y =150)

btn__8 = Button(root, text="8", width= 7, height= 2, bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("8")).place(x=310, y =150)

btn__9 = Button(root, text="9", width= 7, height= 2, bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("9")).place(x=410, y =150)

btn__10= Button(root, text="-", width= 7, height= 2, bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("-")).place(x=10, y =200)

btn__11 = Button(root, text="+", width= 7, height= 2, bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("+")).place(x=110, y =200)

btn__12 = Button(root, text="x", width= 7, height= 2, bg="yellow",bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("*")).place(x=210, y =200)

btn__13 = Button(root, text="/", width= 7, height= 2, bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("/")).place(x=310, y =200)

btn__14 = Button(root, text=".", width= 7, height= 2, bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show(".")).place(x=410, y =200)

btn__15 = Button(root, text="R", width= 7, height= 2, bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("%")).place(x=10, y =250)

btn__16 = Button(root, text="//", width= 7, height= 2,  bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("//")).place(x=110, y =250)

btn__17 = Button(root, text="^", width= 7, height= 2, bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: show("**")).place(x=210, y =250)

btn__19 = Button(root, text="C", width= 16, height= 2, bg="yellow", bd=7, fg ="black", font=("Verdana", 12, "bold"), command=lambda: clear()).place(x=310, y =250)

btn__20 = Button(root, text= "=", width= 34, height= 3, bg="yellow", bd=7, fg ="black", font=("Verdana", 15, "bold"), command=lambda: calculate()) .place(x=10, y =300)


root.mainloop()






            
