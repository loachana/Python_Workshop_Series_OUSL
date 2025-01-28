
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
user_input1 = ""
user_input2 = ""
the_sum = 0
adder = 0

# Function to handle button click event
def plus_button():
    global r
    global user_input1
    global the_sum
    global adder
    
    user_input1 = entry1.get()

    if r == 2:
        adder = user_input1
        the_sum = the_sum + int(adder)
        entry1.delete(0, "end")
        entry1.insert(0, the_sum)
    elif r == 1:
        the_sum = the_sum + int(user_input1)
        entry1.delete(0, "end")
    else:
        the_sum = the_sum + int(adder)
        entry1.delete(0, "end")
        entry1.insert(0, the_sum)

    r = r + 1

    print(the_sum)
    



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
button = tk.Button(root, text="+", command=plus_button)
button.pack(pady=10)

#button2 = tk.Button(root, text="=", command=plus_button)
#button2.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()


