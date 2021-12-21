import tkinter as tk
from tkinter.constants import END, LEFT, NW, TOP
from typing import Sized
from PIL import Image, ImageTk
import os
import time

# Main Program
frame = tk.Tk()
frame.title("Cash Flow Minimizer")
frame.geometry("4000x2000")

path = "D:\program\DJANGO_FOR_EVERYONE\\fig1.png"

def printInput():
    global img
    inp = inputtxt.get(1.0, END)
    f = open("input.txt", "w")
    f.write(inp)
    f.close()
    time.sleep(1)
    os.system("python graph.py")
    time.sleep(1)
    img = ImageTk.PhotoImage(Image.open(path))
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
printButton = tk.Button(frame,text="Solve",command=printInput)
printButton.place(x = 265, y = 580)

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
