
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

# Function to handle button click event
def plus_button():
    global r
    global user_input1
    global user_input2
    global the_sum
    
    if r%2 == 1:
        user_input1 = entry1.get()
        #print(user_input1)
        the_sum = the_sum + int(user_input1)
        if user_input1 == user_input2:
            the_sum = the_sum + int(user_input2)
        else:
            pass
        #entry1.delete(0,"end")
        if r == 1:
            entry1.insert(0, int(user_input1))
            entry1.delete(0,"end")
        else:
            entry1.delete(0,"end")
            entry1.insert(0, the_sum)

        print(the_sum)
        r = r+1
        
    elif r%2 == 0:
        user_input2 = entry1.get()
        
        #print(user_input1)
        the_sum = the_sum + int(user_input2)

        if user_input1 == user_input2:
            the_sum = the_sum + int(user_input1)
        else:
            pass
        
        
       
        entry1.delete(0,"end")
        entry1.insert(0, the_sum)
        r = r+1

        print(the_sum)

    #user_input2 = entry1.get()

    #the_sum = new1 + user_input2
    #entry1.delete(0,"end")
    #entry1.insert(0,the_sum)



root = tk.Tk()
root.title("Get User Name")
root.geometry("300x300")

# Label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Entry widget
entry1 = tk.Entry(root)
entry1.pack(pady=5)


# Button widget
button = tk.Button(root, text="+", command=plus_button)
button.pack(pady=10)

#button2 = tk.Button(root, text="=", command=plus_button)
#button2.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()


