#2/2/2025

#Importing Libraries
import tkinter as tk
from tkinter import messagebox

r=1

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("450x500")

#Lock resizing
root.resizable(False, False)

label = tk.Label(root, text="TIC TAC TOE", font=("Arial", 20))
label.pack(pady=10)

_1x1 = 1
_1x2 = 1
_1x3 = 1
_2x1 = 1
_2x2 = 1
_2x3 = 1
_3x1 = 1
_3x2 = 1
_3x3 = 1

_1x123 = 0
_2x123 = 0
_3x123 = 0
_123x1 = 0
_123x2 = 0
_123x3 = 0
_pri_diagonal = 0
_sec_diagonal = 0


def button_1_c():
    global r
    global _1x1
    global _1x123
    global _123x1
    global _pri_diagonal

    
    if r%2 == 0:
        button_1.config(text="X")
        button_1.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_1.config(text="O")
        button_1.config(state=tk.DISABLED)
    r = r + 1


    _1x123 = _1x123 + _1x1
    _123x1 = _123x1 + _1x1
    _pri_diagonal = _pri_diagonal + _1x1


    if _1x123 == 3:
        print("win")
    elif _123x1 == 3:
        print("win")
    elif _pri_diagonal == 3:
        print("win")


def button_2_c():
    global r
    global _1x2
    if r%2 == 0:
        button_2.config(text="X")
        button_2.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_2.config(text="O")
        button_2.config(state=tk.DISABLED)
    r = r + 1






def button_3_c():
    global r
    global _1x3
    if r%2 == 0:
        button_3.config(text="X")
        button_3.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_3.config(text="O")
        button_3.config(state=tk.DISABLED)
    r = r + 1

    

def button_4_c():
    global r
    global _2x1
    if r%2 == 0:
        button_4.config(text="X")
        button_4.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_4.config(text="O")
        button_4.config(state=tk.DISABLED)
    r = r + 1

    

def button_5_c():
    global r
    global _2x2
    if r%2 == 0:
        button_5.config(text="X")
        button_5.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_5.config(text="O")
        button_5.config(state=tk.DISABLED)
    r = r + 1

    

def button_6_c():
    global r
    global _2x3
    if r%2 == 0:
        button_6.config(text="X")
        button_6.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_6.config(text="O")
        button_6.config(state=tk.DISABLED)
    r = r + 1



def button_7_c():
    global r
    global _3x1
    if r%2 == 0:
        button_7.config(text="X")
        button_7.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_7.config(text="O")
        button_7.config(state=tk.DISABLED)
    r = r + 1



def button_8_c():
    global r
    global _3x2
    if r%2 == 0:
        button_8.config(text="X")
        button_8.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_8.config(text="O")
        button_8.config(state=tk.DISABLED)
    r = r + 1



def button_9_c():
    global r
    global _3x3
    if r%2 == 0:
        button_9.config(text="X")
        button_9.config(state=tk.DISABLED)
    elif r%2 == 1:
        button_9.config(text="O")
        button_9.config(state=tk.DISABLED)
    r = r + 1
     
    




pixel = tk.PhotoImage(width=1, height=1)


button_1 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_1_c, font=("Arial", 50))
button_1.place(x=0, y=50)

button_2 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_2_c, font=("Arial", 50))
button_2.place(x=150, y=50)

button_3 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_3_c, font=("Arial", 50))
button_3.place(x=300, y=50)

button_4 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_4_c, font=("Arial", 50))
button_4.place(x=0, y=200)

button_5 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_5_c, font=("Arial", 50))
button_5.place(x=150, y=200)

button_6 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_6_c, font=("Arial", 50))
button_6.place(x=300, y=200)

button_7 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_7_c, font=("Arial", 50))
button_7.place(x=0, y=350)

button_8 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_8_c, font=("Arial", 50))
button_8.place(x=150, y=350)

button_9 = tk.Button(root, image=pixel, compound="c", height=150, width=150, command= button_9_c, font=("Arial", 50))
button_9.place(x=300, y=350)

#Calling mainloop
root.mainloop()
