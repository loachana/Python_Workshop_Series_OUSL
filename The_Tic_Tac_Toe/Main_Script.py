#2/2/2025

#Importing Libraries
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")

#Lock resizing
root.resizable(False, False)

label = tk.Label(root, text="TIC TAC TOE", font=("Arial", 20))
label.pack(pady=10)

button_plus = tk.Button(root, text=" + ", font=("Arial", 30), height=3, width=3)
button_plus.place(x=400, y=320)
               
#Calling mainloop
root.mainloop()
