import tkinter as tk

input_1_p = 0
input_1_min = 0
input_1_mult = 0
input_1_div = 0


the_sum = 0
the_min = 0
the_div = 0
the_mult = 0

input_2 = 0

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

def button_1():
    entry1.insert(tk.END,1)

#------------------------------------------------------

def button_2():
    entry1.insert(tk.END,2)

#------------------------------------------------------

def button_3():
    entry1.insert(tk.END,3)

#------------------------------------------------------

def button_4():
    entry1.insert(tk.END,4)

#------------------------------------------------------

def button_5():
    entry1.insert(tk.END,5)

#------------------------------------------------------

def button_6():
    entry1.insert(tk.END,6)

#------------------------------------------------------

def button_7():
    entry1.insert(tk.END,7)

#------------------------------------------------------

def button_8():
    entry1.insert(tk.END,8)

#------------------------------------------------------

def button_9():
    entry1.insert(tk.END,9)

#------------------------------------------------------

def button_0():
    entry1.insert(tk.END,0)

#------------------------------------------------------

def dot_button():
    entry1.insert(tk.END,'.')
    
#------------------------------------------------------
def clear_entry_button():
    entry1.delete(0, 'end')
#------------------------------------------------------


root = tk.Tk()
root.title("The Simple Calculator")
root.geometry("500x500")

root.resizable(False, False)

# Label
label = tk.Label(root, text="THE SIMPLE CALCULATOR", font=("Arial", 20))
label.pack(pady=10)

# Entry widget
entry1 = tk.Entry(root, width=22, font=('Arial 30'), justify="right")
entry1.pack(pady=5)

# Button widget
button_plus = tk.Button(root, text=" + ", command=plus_button, font=("Arial", 30), height=3, width=3)
button_plus.place(x=400, y=320)

button_minus = tk.Button(root, text=" - ", command=minus_button, font=("Arial", 30), height=1, width=3)
button_minus.place(x=312, y=324)

button_clear = tk.Button(root, text=" C ", command=clear_button, font=("Arial", 30), height=1, width=3)
button_clear.place(x=312, y=125)

button_1 = tk.Button(root, text=" 1 ", command=button_1, font=("Arial", 30), height=1, width=3)
button_1.place(x=25, y=325)

button_2 = tk.Button(root, text=" 2 ", command=button_2, font=("Arial", 30), height=1, width=3)
button_2.place(x=125, y=325)

button_3 = tk.Button(root, text=" 3 ", command=button_3, font=("Arial", 30), height=1, width=3)
button_3.place(x=225, y=325)

button_4 = tk.Button(root, text=" 4 ", command=button_4, font=("Arial", 30), height=1, width=3)
button_4.place(x=25, y=225)

button_5 = tk.Button(root, text=" 5 ", command=button_5, font=("Arial", 30), height=1, width=3)
button_5.place(x=125, y=225)

button_6 = tk.Button(root, text=" 6 ", command=button_6, font=("Arial", 30), height=1, width=3)
button_6.place(x=225, y=225)

button_7 = tk.Button(root, text=" 7 ", command=button_7, font=("Arial", 30), height=1, width=3)
button_7.place(x=25, y=125)

button_8 = tk.Button(root, text=" 8 ", command=button_8, font=("Arial", 30), height=1, width=3)
button_8.place(x=125, y=125)

button_9 = tk.Button(root, text=" 9 ", command=button_9, font=("Arial", 30), height=1, width=3)
button_9.place(x=225, y=125)

button_0 = tk.Button(root, text=" 0 ", command=button_0, font=("Arial", 30), height=1, width=7)
button_0.place(x=28, y=412)

button_equals = tk.Button(root, text=" = ", command=equals_button, font=("Arial", 30), height=1, width=3)
button_equals.place(x=312, y=411)

button_minus = tk.Button(root, text=" X ", command=mult_button, font=("Arial", 30), height=1, width=3)
button_minus.place(x=400, y=225)

button_minus = tk.Button(root, text=" ÷ ", command=div_button, font=("Arial", 30), height=1, width=3)
button_minus.place(x=400, y=125)

button_equals = tk.Button(root, text=" . ", command=dot_button, font=("Arial", 30), height=1, width=3)
button_equals.place(x=225, y=411)

button_clear = tk.Button(root, text=" CE ", command=clear_entry_button, font=("Arial", 30), height=1, width=3)
button_clear.place(x=312, y=225)

root.mainloop()
