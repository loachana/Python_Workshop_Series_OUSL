
'''
def addition(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result

def division(num1, num2):
    result = num1 / num2
    return result

'''

import tkinter as tk

r = 1
p = 1
n = 1
user_input1 = ""
user_input2 = ""
the_plus = 0
adder = 0
the_sub = 0
minor = 0
the_sum = 0
secondnumber = 0


# Function to handle button click event
def plus_button():
    global r
    global user_input1
    global the_plus
    global adder
    
    user_input1 = entry1.get()
    the_plus = int(user_input1)
    entry1.delete(0,"end")

    '''  
    if r == 2:
        adder = user_input1
        the_plus = the_plus + int(adder)
        entry1.delete(0, "end")
        #entry1.insert(0, the_plus)
    elif r == 1:
        the_plus = the_plus + int(user_input1)
        entry1.delete(0, "end")
    else:
        the_plus = the_plus + int(user_input1)
        entry1.delete(0, "end")
        #entry1.insert(0, the_plus)
    '''    
    return the_plus

#---------------------------------------------------------
def minus_button():
    global p
    global user_input1
    global the_sub
    global minor
    
    user_input1 = entry1.get()

    if p == 2:
        minor = user_input1
        the_sub = the_sub - int(minor)
        entry1.delete(0, "end")
        entry1.insert(0, the_sub)
    elif p == 1:
        the_sub = the_sub + int(user_input1)
        entry1.delete(0, "end")
    else:
        the_sub = the_sub - int(user_input1)
        entry1.delete(0, "end")
        entry1.insert(0, the_sub)

    p = p + 1

    print(the_sub)    

#--------------------------------------------------------------

def clear_button():
    global r
    global user_input1
    global the_sum
    global adder
    global minor
    
    entry1.delete(0, 'end')

    r = 1
    the_sum = 0
    the_sub=0
    adder = 0
    minor = 0
    the_plus = 0

    user_input1 = ''

#-------------------------------------------------------------
def equals_button():
    global n
    global user_input1
    global user_input2
    global the_plus
    global adder
    global the_sum
    global secondnumber

    user_input2 = entry1.get()
    if n == 1:
        secondnumber = int(user_input2)
    else:
        pass
    the_sum = n*secondnumber + the_plus
    entry1.delete(0, "end")
    entry1.insert(tk.END,the_sum)
    print(the_sum)
    
    n = n + 1   
#------------------------------------------------------

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

#-------------------------------------------------------

root = tk.Tk()
root.title("The Simple Calculator")
root.geometry("600x600")

# Label
label = tk.Label(root, text="The Simple Calculator", font=("Arial", 20))
label.pack(pady=10)

# Entry widget
entry1 = tk.Entry(root, width=100, font=('Arial 30'), justify="right")
entry1.pack(pady=5)


# Button widget
button_plus = tk.Button(root, text=" + ", command=plus_button, font=("Arial", 30))
button_plus.place(x=500, y=400)

button_minus = tk.Button(root, text=" - ", command=minus_button, font=("Arial", 30))
button_minus.place(x=500, y=300)

button_clear = tk.Button(root, text=" C ", command=clear_button, font=("Arial", 30))
button_clear.place(x=400, y=400)

button_1 = tk.Button(root, text=" 1 ", command=button_1, font=("Arial", 30))
button_1.place(x=100, y=400)

button_2 = tk.Button(root, text=" 2 ", command=button_2, font=("Arial", 30))
button_2.place(x=200, y=400)

button_3 = tk.Button(root, text=" 3 ", command=button_3, font=("Arial", 30))
button_3.place(x=300, y=400)

button_4 = tk.Button(root, text=" 4 ", command=button_4, font=("Arial", 30))
button_4.place(x=100, y=300)

button_5 = tk.Button(root, text=" 5 ", command=button_5, font=("Arial", 30))
button_5.place(x=200, y=300)

button_6 = tk.Button(root, text=" 6 ", command=button_6, font=("Arial", 30))
button_6.place(x=300, y=300)

button_7 = tk.Button(root, text=" 7 ", command=button_7, font=("Arial", 30))
button_7.place(x=100, y=200)

button_8 = tk.Button(root, text=" 8 ", command=button_8, font=("Arial", 30))
button_8.place(x=200, y=200)

button_9 = tk.Button(root, text=" 9 ", command=button_9, font=("Arial", 30))
button_9.place(x=300, y=200)

button_0 = tk.Button(root, text=" 0 ", command=button_0, font=("Arial", 30))
button_0.place(x=200, y=500)

button_equals = tk.Button(root, text=" = ", command=equals_button, font=("Arial", 30))
button_equals.place(x=400, y=500)



#button2 = tk.Button(root, text="=", command=plus_button)
#button2.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()


