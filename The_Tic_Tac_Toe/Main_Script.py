#2/2/2025

#Importing Libraries
import tkinter as tk
from tkinter import messagebox

r = 0
                
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

o_1x123 = 0
o_2x123 = 0
o_3x123 = 0
o_123x1 = 0
o_123x2 = 0
o_123x3 = 0
o_pri_diagonal = 0
o_sec_diagonal = 0


x_1x123 = 0
x_2x123 = 0
x_3x123 = 0
x_123x1 = 0
x_123x2 = 0
x_123x3 = 0
x_pri_diagonal = 0
x_sec_diagonal = 0

'''

global o_1x123
global o_2x123
global o_3x123
global o_123x1
global o_123x2
global o_123x3
global o_pri_diagonal
global o_sec_diagonal

global x_1x123
global x_2x123
global x_3x123
global x_123x1
global x_123x2
global x_123x3
global x_pri_diagonal
global x_sec_diagonal

'''

def ResetBomb():
    global r
    
    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal


    
    button_1.config(bg="#f0f0f0", state=tk.NORMAL, text="")
    button_2.config(bg="#f0f0f0", state=tk.NORMAL, text="")
    button_3.config(bg="#f0f0f0", state=tk.NORMAL, text="")

    button_4.config(bg="#f0f0f0", state=tk.NORMAL, text="")
    button_5.config(bg="#f0f0f0", state=tk.NORMAL, text="")
    button_6.config(bg="#f0f0f0", state=tk.NORMAL, text="")
    button_7.config(bg="#f0f0f0", state=tk.NORMAL, text="")
    button_8.config(bg="#f0f0f0", state=tk.NORMAL, text="")
    button_9.config(bg="#f0f0f0", state=tk.NORMAL, text="")

    o_1x123 = 0
    o_2x123 = 0
    o_3x123 = 0
    o_123x1 = 0
    o_123x2 = 0
    o_123x3 = 0
    o_pri_diagonal = 0
    o_sec_diagonal = 0

    x_1x123 = 0
    x_2x123 = 0
    x_3x123 = 0
    x_123x1 = 0
    x_123x2 = 0
    x_123x3 = 0
    x_pri_diagonal = 0
    x_sec_diagonal = 0

    r = 0

    
def button_1_c():
    global r
    global _1x1
    
    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal
    
    
    if r%2 == 0:
        button_1.config(text="X")
        button_1.config(state=tk.DISABLED)
        
        x_1x123 = x_1x123 + _1x1
        x_123x1 = x_123x1 + _1x1
        x_pri_diagonal = x_pri_diagonal + _1x1

        r = r + 1

        if x_1x123 == 3:
            button_1.config(bg="#FFD580")
            button_2.config(bg="#FFD580")
            button_3.config(bg="#FFD580")
            
            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

    
        elif x_123x1 == 3:
            button_1.config(bg="#FFD580")
            button_4.config(bg="#FFD580")
            button_7.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif x_pri_diagonal == 3:
            button_1.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()


        
    elif r%2 == 1:
        button_1.config(text="O")
        button_1.config(state=tk.DISABLED)

        o_1x123 = o_1x123 + _1x1
        o_123x1 = o_123x1 + _1x1
        o_pri_diagonal = o_pri_diagonal + _1x1

        r = r + 1

        if o_1x123 == 3:
            button_1.config(bg="#90EE90")
            button_2.config(bg="#90EE90")
            button_3.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x1 == 3:
            button_1.config(bg="#90EE90")
            button_4.config(bg="#90EE90")
            button_7.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_pri_diagonal == 3:
            button_1.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()


'''
    _1x123 = _1x123 + _1x1
    _123x1 = _123x1 + _1x1
    _pri_diagonal = _pri_diagonal + _1x1


    if _1x123 == 3:
        print("win")
    elif _123x1 == 3:
        print("win")
    elif _pri_diagonal == 3:
        print("win")
'''


def button_2_c():
    global r
    global _1x2

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal

    
    if r%2 == 0:
        button_2.config(text="X")
        button_2.config(state=tk.DISABLED)

        x_1x123 = x_1x123 + _1x2
        x_123x2 = x_123x2 + _1x2

        r = r + 1

        if x_1x123 == 3:
            button_1.config(bg="#FFD580")
            button_2.config(bg="#FFD580")
            button_3.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x2 == 3:
            button_2.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_8.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()
            
            
    elif r%2 == 1:
        button_2.config(text="O")
        button_2.config(state=tk.DISABLED)

        o_1x123 = o_1x123 + _1x2
        o_123x2 = o_123x2 + _1x2

        r = r + 1

        if o_1x123 == 3:
            button_1.config(bg="#90EE90")
            button_2.config(bg="#90EE90")
            button_3.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x2 == 3:
            button_2.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_8.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()

    
            
'''
    _1x123 = _1x123 + _1x2
    _123x2 = _123x2 + _1x2
    
    if _1x123 == 3:
        print("win")
    elif _123x2 == 3:
        print("win")
'''


def button_3_c():
    global r
    global _1x3

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal
    
    if r%2 == 0:
        button_3.config(text="X")
        button_3.config(state=tk.DISABLED)

        x_1x123 = x_1x123 + _1x3
        x_123x3 = x_123x3 + _1x3
        x_sec_diagonal = x_sec_diagonal + _1x3

        r = r + 1

        if x_1x123 == 3:
            button_1.config(bg="#FFD580")
            button_2.config(bg="#FFD580")
            button_3.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x3 == 3:
            button_3.config(bg="#FFD580")
            button_6.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_sec_diagonal == 3:
            button_3.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_7.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()
            

        
    elif r%2 == 1:
        button_3.config(text="O")
        button_3.config(state=tk.DISABLED)

        o_1x123 = o_1x123 + _1x3
        o_123x3 = o_123x3 + _1x3
        o_sec_diagonal = o_sec_diagonal + _1x3

        r = r + 1

        if o_1x123 == 3:
            button_1.config(bg="#90EE90")
            button_2.config(bg="#90EE90")
            button_3.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x3 == 3:
            button_3.config(bg="#90EE90")
            button_6.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_sec_diagonal == 3:
            button_3.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_7.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()



'''
    _1x123 = _1x123 + _1x3
    _123x3 = _123x3 + _1x3
    _sec_diagonal = _sec_diagonal + _1x3

    if _1x123 == 3:
        print("win")
    elif _123x3 == 3:
        print("win")
    elif _sec_diagonal == 3:
        print("win")
'''
    

def button_4_c():
    global r
    global _2x1

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal


    if r%2 == 0:
        button_4.config(text="X")
        button_4.config(state=tk.DISABLED)

        x_2x123 = x_2x123 + _2x1
        x_123x1 = x_123x1 + _2x1

        r = r + 1

        if x_2x123 == 3:
            button_4.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_6.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x1 == 3:
            button_1.config(bg="#FFD580")
            button_4.config(bg="#FFD580")
            button_7.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()
            


    elif r%2 == 1:
        button_4.config(text="O")
        button_4.config(state=tk.DISABLED)

        o_2x123 = o_2x123 + _2x1
        o_123x1 = o_123x1 + _2x1

        r = r + 1

        if o_2x123 == 3:
            button_4.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_6.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x1 == 3:
            button_1.config(bg="#90EE90")
            button_4.config(bg="#90EE90")
            button_7.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()


'''
    _2x123 = _2x123 + _2x1
    _123x1 = _123x1 + _2x1

    if _2x123 == 3:
        print("win")
    elif _123x1 == 3:
        print("win")

'''    

def button_5_c():
    global r
    global _2x2

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal


    if r%2 == 0:
        button_5.config(text="X")
        button_5.config(state=tk.DISABLED)

        x_2x123 = x_2x123 + _2x2
        x_123x2 = x_123x2 + _2x2
        x_pri_diagonal = x_pri_diagonal + _2x2
        x_sec_diagonal = x_sec_diagonal + _2x2

        r = r + 1


        if x_2x123 == 3:
            button_4.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_6.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x2 == 3:
            button_2.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_8.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_pri_diagonal == 3:
            button_1.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_sec_diagonal == 3:
            button_3.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_7.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()
            

        
    elif r%2 == 1:
        button_5.config(text="O")
        button_5.config(state=tk.DISABLED)

        o_2x123 = o_2x123 + _2x2
        o_123x2 = o_123x2 + _2x2
        o_pri_diagonal = o_pri_diagonal + _2x2
        o_sec_diagonal = o_sec_diagonal + _2x2

        r = r + 1


        if o_2x123 == 3:
            button_4.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_6.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x2 == 3:
            button_2.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_8.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_pri_diagonal == 3:
            button_1.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_sec_diagonal == 3:
            button_3.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_7.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()



'''
    _2x123 = _2x123 + _2x2
    _123x2 = _123x2 + _2x2
    _pri_diagonal = _pri_diagonal + _2x2
    _sec_diagonal = _sec_diagonal + _2x2


    if _2x123 == 3:
        print("win")
    elif _123x2 == 3:
        print("win")
    elif _pri_diagonal == 3:
        print("win")
    elif _sec_diagonal == 3:
        print("win")
 '''


def button_6_c():
    global r
    global _2x3

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal

    if r%2 == 0:
        button_6.config(text="X")
        button_6.config(state=tk.DISABLED)
        
        x_2x123 = x_2x123 + _2x3
        x_123x3 = x_123x3 + _2x3

        r = r + 1

        if x_2x123 == 3:
            button_4.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_6.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x3 == 3:
            button_3.config(bg="#FFD580")
            button_6.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()
            
            
    elif r%2 == 1:
        button_6.config(text="O")
        button_6.config(state=tk.DISABLED)

        o_2x123 = o_2x123 + _2x3
        o_123x3 = o_123x3 + _2x3

        r = r + 1

        if o_2x123 == 3:
            button_4.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_6.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x3 == 3:
            button_3.config(bg="#90EE90")
            button_6.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()



'''
    _2x123 = _2x123 + _2x3
    _123x3 = _123x3 + _2x3

    if _2x123 == 3:
        print("win")
    elif _123x3 == 3:
        print("win")
'''


def button_7_c():
    global r
    global _3x1

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal

    
    if r%2 == 0:
        button_7.config(text="X")
        button_7.config(state=tk.DISABLED)

        x_3x123 = x_3x123 + _3x1
        x_123x1 = x_123x1 + _3x1
        x_sec_diagonal = x_sec_diagonal + _3x1

        r = r + 1
            
        if x_3x123 == 3:
            button_7.config(bg="#FFD580")
            button_8.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x1 == 3:
            button_1.config(bg="#FFD580")
            button_4.config(bg="#FFD580")
            button_7.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_sec_diagonal == 3:
            button_3.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_7.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()
            


    elif r%2 == 1:
        button_7.config(text="O")
        button_7.config(state=tk.DISABLED)

        o_3x123 = o_3x123 + _3x1
        o_123x1 = o_123x1 + _3x1
        o_sec_diagonal = o_sec_diagonal + _3x1

        r = r + 1
            
        if o_3x123 == 3:
            button_7.config(bg="#90EE90")
            button_8.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x1 == 3:
            button_1.config(bg="#90EE90")
            button_4.config(bg="#90EE90")
            button_7.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_sec_diagonal == 3:
            button_3.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_7.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()




'''
    _3x123 = _3x123 + _3x1
    _123x1 = _123x1 + _3x1
    _sec_diagonal = _sec_diagonal + _3x1

    if _3x123 == 3:
        print("win")
    elif _123x1 == 3:
        print("win")
    elif _sec_diagonal == 3:
        print("win")
'''


def button_8_c():
    global r
    global _3x2

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal


    
    if r%2 == 0:
        button_8.config(text="X")
        button_8.config(state=tk.DISABLED)

        x_3x123 = x_3x123 + _3x2
        x_123x2 = x_123x2 + _3x2

        r = r + 1

        if x_3x123 == 3:
            button_7.config(bg="#FFD580")
            button_8.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x2 == 3:
            button_2.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_8.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()
    
        
    elif r%2 == 1:
        button_8.config(text="O")
        button_8.config(state=tk.DISABLED)

        o_3x123 = o_3x123 + _3x2
        o_123x2 = o_123x2 + _3x2

        r = r + 1

        if o_3x123 == 3:
            button_7.config(bg="#90EE90")
            button_8.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x2 == 3:
            button_2.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_8.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()



'''
    _3x123 = _3x123 + _3x2
    _123x2 = _123x2 + _3x2

    if _3x123 == 3:
        print("win")
    elif _123x2 == 3:
        print("win")
'''


def button_9_c():
    global r
    global _3x3

    global o_1x123
    global o_2x123
    global o_3x123
    global o_123x1
    global o_123x2
    global o_123x3
    global o_pri_diagonal
    global o_sec_diagonal

    global x_1x123
    global x_2x123
    global x_3x123
    global x_123x1
    global x_123x2
    global x_123x3
    global x_pri_diagonal
    global x_sec_diagonal

    
    if r%2 == 0:
        button_9.config(text="X")
        button_9.config(state=tk.DISABLED)

        x_3x123 = x_3x123 + _3x3
        x_123x3 = x_123x3 + _3x3
        x_pri_diagonal = x_pri_diagonal + _3x3

        r = r + 1

        if x_3x123 == 3:
            button_7.config(bg="#FFD580")
            button_8.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_123x3 == 3:
            button_3.config(bg="#FFD580")
            button_6.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()
            
        elif x_pri_diagonal == 3:
            button_1.config(bg="#FFD580")
            button_5.config(bg="#FFD580")
            button_9.config(bg="#FFD580")

            messagebox.showinfo("Congratulations!", "Player 1 wins!")

            ResetBomb()

        elif r == 9:

            messagebox.showinfo("Game tie", "It is a tie!")

            ResetBomb()


    elif r%2 == 1:
        button_9.config(text="O")
        button_9.config(state=tk.DISABLED)

        o_3x123 = o_3x123 + _3x3
        o_123x3 = o_123x3 + _3x3
        o_pri_diagonal = o_pri_diagonal + _3x3

        r = r + 1

        if o_3x123 == 3:
            button_7.config(bg="#90EE90")
            button_8.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_123x3 == 3:
            button_3.config(bg="#90EE90")
            button_6.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()
            
        elif o_pri_diagonal == 3:
            button_1.config(bg="#90EE90")
            button_5.config(bg="#90EE90")
            button_9.config(bg="#90EE90")

            messagebox.showinfo("Congratulations!", "Player 2 wins!")

            ResetBomb()



     
'''    
    _3x123 = _3x123 + _3x3
    _123x3 = _123x3 + _3x3
    _pri_diagonal = _pri_diagonal + _3x3

    if _3x123 == 3:
        print("win")
    elif _123x3 == 3:
        print("win")
    elif _pri_diagonal == 3:
        print("win")

'''

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
