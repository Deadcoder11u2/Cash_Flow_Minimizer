import tkinter as tk
from tkinter.constants import END, LEFT, NW, TOP
from typing import Sized
from PIL import Image, ImageTk
import os
import time
from matplotlib.pyplot import legend

# Main Program
frame = tk.Tk()
frame.title("Cash Flow Minimizer")
frame.geometry("4000x2000")

path = "D:\program\DJANGO_FOR_EVERYONE\\fig1.png"

def printInput():
    global img
    os.system("python graph.py")
    time.sleep(1)
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(frame, image = img)
    panel.place(x = 625, y = 90)


def plotInput():
    global img
    inp = inputtxt.get(1.0, END)
    f = open("input.txt", "w")
    f.write(inp)
    f.close()
    time.sleep(0.5)
    os.system("python inputplot.py")
    time.sleep(0.5)
    img = ImageTk.PhotoImage(Image.open("D:\program\DJANGO_FOR_EVERYONE\\fig2.png"))
    panel = tk.Label(frame, image = img)
    panel.place(x = 625, y = 90)

# Header Creation
project_titile = ImageTk.PhotoImage(Image.open("header.png"))
panel_header = tk.Label(frame, image=project_titile)
panel_header.place(x = 350, y = 20)

# TextBox Creation
inputtxt = tk.Text(frame,height=23,width=65, font=('Times New Roman', 14))
inputtxt.place(x = 10, y = 90)

# Button Creation
InputButton = tk.Button(frame,text="Plot Input", command=plotInput)
InputButton.place(x = 265, y = 580)
printButton = tk.Button(frame,text="Plot Output",command=printInput)
printButton.place(x = 262, y = 610)

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()