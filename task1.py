"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
win = tk.Tk()

def run():
    name = NameData.get()
    number = NumberData.get()
    grade = GradeData.get()
    total = name + number + grade
    TotalData = total
    Result = TotalData.config(text = TotalData)

NameData = tk.StringVar()
NumberData = tk.StringVar()
GradeData = tk.StringVar()
TotalData = tk.StringVar()

Name = tk.Entry(win,width=15,textvariable=NameData)
Number = tk.Entry(win,width=15,textvariable=NumberData)
Grade = tk.Entry(win,width=15,textvariable=GradeData)
l1 = tk.Label(win,text="Name")
l2 = tk.Label(win,text="Number")
l3 = tk.Label(win,text="Grade")
b1 = tk.Button(win,text="Click")
Result = tk.Entry(win,width=15,textvariable=TotalData)

b1.bind("<Button-1>",run)

l1.pack()
Name.pack()
l2.pack()
Number.pack()
l3.pack()
Grade.pack()
b1.pack()
Result.pack()

win.mainloop()
