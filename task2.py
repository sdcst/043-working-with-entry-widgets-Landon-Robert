#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk
import math
win = tk.Tk()

def run(e):
    Number1 = Number1Data.get()
    Number2 = Number2Data.get()
    total = (float(Number1)**2 + float(Number2)**2)**0.5
    
    Result.delete(0, tk.END)
    Result.insert(0, total)

Number1Data = tk.IntVar()
Number2Data = tk.IntVar()
TotalData = tk.IntVar()

l1 = tk.Label(win,text="Number1")
l2 = tk.Label(win,text="Number2")
l3 = tk.Label(win,text="Hypotenuse: ")
Box1 = tk.Entry(win,width=15,textvariable=Number1Data)
Box2 = tk.Entry(win,width=15,textvariable=Number2Data)
b1 = tk.Button(win,text="Hyp")
Result = tk.Entry(win,width=50,textvariable=TotalData)

b1.bind("<Button-1>",run)

l1.pack()
Box1.pack()
l2.pack()
Box2.pack()
b1.pack()
Result.pack()

win.mainloop()