from tkinter import *
from BackEnd import BackEnd


class FrontEnd:
    def __init__(self):
        BE = BackEnd()
        master = Tk()
        greeting = Label(master,bg = "#0059b3",
                         text="Hello! This is a program that displays the temperature differential from the baseline\n"
                              "Celcius average from 1960-1990. "
                              , font=28)
        greeting.pack()
        b1 = Button(master, font=21, text="XY plot", fg="red", bg="yellow",width=20, height=20, command=BE.XYplot)
        b2 = Button(master, font=21,text='Bar chart', fg="green", bg = "white", width=20, height=20,
                    command=BE.BarChart)
        b3 = Button(master, font=21,text="Linear Regression", fg="blue", bg="black", width=20, height=20,
                    command=BE.LinearRegression)
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        master.title("Lab 1")
        master.geometry("630x370")
        master.configure(bg = "#49A")
        master.mainloop()
