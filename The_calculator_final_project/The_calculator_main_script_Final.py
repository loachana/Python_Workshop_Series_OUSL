#28/01/2025
#This is the codebase in response to final project of the Python Workshop Series OUSL
#All Rights Reserved!
#This codebase is fully open-source and all suggestions are welcome.


#THE SIMPLE CALCULATOR is a very basic arithmatic calculator.
#It can handle main four operations with limitations.

#Importing Libraries
import tkinter as tk
from tkinter import messagebox

#Defining global variables
input_1_p = 0
input_1_min = 0
input_1_mult = 0
input_1_div = 0

the_sum = 0
the_min = 0
the_div = 0
the_mult = 0

input_2 = 0
#-------------------------------------------------------------------------

#The plus button
def plus_button():

    global input_1_p

    try:
        input_1_p = float(entry1.get())
        entry1.delete(0, 'end')
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "ERROR")
    
    
    return input_1_p

#-------------------------------------------------------------------------

#The minus button
def minus_button():

    global input_1_min 

    try:
        input_1_min = float(entry1.get())
        entry1.delete(0, 'end')
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "ERROR")

    return input_1_min
#-------------------------------------------------------------------------

#The multiplication button
def mult_button():

    global input_1_mult

    try:
        input_1_mult = float(entry1.get())
        entry1.delete(0, 'end')
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "ERROR")

    return input_1_mult


#------------------------------------------------------------------------

#The division button
def div_button():
    global input_1_div

    try:
        input_1_div = float(entry1.get())
        entry1.delete(0, 'end')
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "ERROR")

    return input_1_div

    
#-------------------------------------------------------------------------

#The equals button
def equals_button():
    
    global input_1_p
    global input_1_min
    global input_1_mult
    global input_1_div
    global the_sum
    global the_min
    global the_div
    global the_mult
    global input_2
    

    try:
        input_2 = float(entry1.get())
        entry1.delete(0, 'end')

        if input_1_p != 0:
            the_sum = input_1_p + input_2
            entry1.insert(0, the_sum)
        elif input_1_min != 0:
            the_min = input_1_min - input_2
            entry1.insert(0, the_min)
        elif input_1_mult != 0 :
            the_mult = input_1_mult*input_2
            entry1.insert(0, the_mult)
        elif input_1_div != 0:
            if input_2 == 0:
                entry1.insert(0, "INVALID OPERATION")
            else:
                the_div = input_1_div/input_2
                entry1.insert(0, the_div)
        else:
            pass
  
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "ERROR")


    input_1_p = 0
    input_1_min = 0
    input_1_mult = 0
    input_1_div = 0


    the_sum = 0
    the_min = 0
    the_div = 0
    the_mult = 0

    input_2 = 0


#--------------------------------------------------------------------------

#The clear button
def clear_button():

    global input_1_p
    global input_1_min
    global input_1_mult
    global input_1_div
    global the_sum
    global the_min
    global the_div
    global the_mult
    global input_2
    
    input_1_p = 0
    input_1_min = 0
    input_1_mult = 0
    input_1_div = 0


    the_sum = 0
    the_min = 0
    the_div = 0
    the_mult = 0

    input_2 = 0

    entry1.delete(0, 'end')

#-----------------------------------------------------
#Button 1 command function
def button_1():
    entry1.insert(tk.END,1)

#------------------------------------------------------
#Button 2 command function
def button_2():
    entry1.insert(tk.END,2)

#------------------------------------------------------
#Button 3 command function
def button_3():
    entry1.insert(tk.END,3)

#------------------------------------------------------
#Button 4 command function
def button_4():
    entry1.insert(tk.END,4)

#------------------------------------------------------
#Button 5 command function
def button_5():
    entry1.insert(tk.END,5)

#------------------------------------------------------
#Button 6 command function
def button_6():
    entry1.insert(tk.END,6)

#------------------------------------------------------
#Button 7 command function
def button_7():
    entry1.insert(tk.END,7)

#------------------------------------------------------
#Button 8 command function
def button_8():
    entry1.insert(tk.END,8)

#------------------------------------------------------
#Button 9 command function
def button_9():
    entry1.insert(tk.END,9)

#------------------------------------------------------
#Button 0 command function
def button_0():
    entry1.insert(tk.END,0)

#------------------------------------------------------
#The dot button command function
def dot_button():
    entry1.insert(tk.END,'.')
    
#------------------------------------------------------
#Entry clear button command function
def clear_entry_button():
    entry1.delete(0, 'end')
#------------------------------------------------------
#About button command function
def about_button():
    messagebox.showinfo("About","""THE SIMPLE CALCULATOR is an open-sourse project.
It is full functioned calculator powered by python language and its built in functions.
Thank you for your interest.

                    © 2025 Lochana Egodawele""")
#------------------------------------------------------

    
root = tk.Tk()
root.title("The Simple Calculator")
root.geometry("500x500")

#Lock resizing
root.resizable(False, False)

#--------------------------------------------------------------------------
#Label - The Head
label = tk.Label(root, text="THE SIMPLE CALCULATOR", font=("Arial", 20))
label.pack(pady=10)

#-----------------------------------------------------------------------------
#Entry widget - Display Area
entry1 = tk.Entry(root, width=22, font=('Arial 30'), justify="right")
entry1.pack(pady=5)

#-------------------------------------------------------------------------------------------------------------------
#Button widgets
#Calling buttons and placing them

#Plus button definitions
button_plus = tk.Button(root, text=" + ", command=plus_button, font=("Arial", 30), height=3, width=3)
button_plus.place(x=400, y=320)

#Minus button definitions
button_minus = tk.Button(root, text=" - ", command=minus_button, font=("Arial", 30), height=1, width=3)
button_minus.place(x=312, y=324)

#clear button definitions
button_clear = tk.Button(root, text=" C ", command=clear_button, font=("Arial", 30), height=1, width=3)
button_clear.place(x=312, y=125)

#Button 1 definitions
button_1 = tk.Button(root, text=" 1 ", command=button_1, font=("Arial", 30), height=1, width=3)
button_1.place(x=25, y=325)

#Button 2 definitions
button_2 = tk.Button(root, text=" 2 ", command=button_2, font=("Arial", 30), height=1, width=3)
button_2.place(x=125, y=325)

#Button 3 definitions
button_3 = tk.Button(root, text=" 3 ", command=button_3, font=("Arial", 30), height=1, width=3)
button_3.place(x=225, y=325)

#Button 4 definitions
button_4 = tk.Button(root, text=" 4 ", command=button_4, font=("Arial", 30), height=1, width=3)
button_4.place(x=25, y=225)

#Button 5 definitions
button_5 = tk.Button(root, text=" 5 ", command=button_5, font=("Arial", 30), height=1, width=3)
button_5.place(x=125, y=225)

#Button 6 definitions
button_6 = tk.Button(root, text=" 6 ", command=button_6, font=("Arial", 30), height=1, width=3)
button_6.place(x=225, y=225)

#Button 7 definitions
button_7 = tk.Button(root, text=" 7 ", command=button_7, font=("Arial", 30), height=1, width=3)
button_7.place(x=25, y=125)

#Button 8 definitions
button_8 = tk.Button(root, text=" 8 ", command=button_8, font=("Arial", 30), height=1, width=3)
button_8.place(x=125, y=125)

#Button 9 definitions
button_9 = tk.Button(root, text=" 9 ", command=button_9, font=("Arial", 30), height=1, width=3)
button_9.place(x=225, y=125)

#Button 0 definitions
button_0 = tk.Button(root, text=" 0 ", command=button_0, font=("Arial", 30), height=1, width=7)
button_0.place(x=28, y=412)

#Equals button definitions
button_equals = tk.Button(root, text=" = ", command=equals_button, font=("Arial", 30), height=1, width=3)
button_equals.place(x=312, y=411)

#Multiplication button definitions
button_mult = tk.Button(root, text=" X ", command=mult_button, font=("Arial", 30), height=1, width=3)
button_mult.place(x=400, y=225)

#Division button definitions
button_div = tk.Button(root, text=" ÷ ", command=div_button, font=("Arial", 30), height=1, width=3)
button_div.place(x=400, y=125)

#Dot button definitions
button_dot = tk.Button(root, text=" . ", command=dot_button, font=("Arial", 30), height=1, width=3)
button_dot.place(x=225, y=411)

#Crear entry button definitions
button_clear_entry = tk.Button(root, text=" CE ", command=clear_entry_button, font=("Arial", 30), height=1, width=3)
button_clear_entry.place(x=312, y=225)

#About button definitions
button_clear_entry = tk.Button(root, text="About", command=about_button, font=("Arial", 10), height=1, width=4)
button_clear_entry.place(x=452, y=5)

#-------------------------------------------------------------------------------------------------------------------
#Calling mainloop
root.mainloop()
