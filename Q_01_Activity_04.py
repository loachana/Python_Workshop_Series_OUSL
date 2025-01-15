#15/1/2025
#This is the code for Q1 in activity 4 of python workshop @ OUSL
#All rights reserved 

#>> We use while toop to keep asking integers from the user.
#>> We also use Try-Except block to prevent the user to enter invalid input.
#>> Inside the loop, We use If statement to cassify the integer given by the user.

#The head
print("THE EVEN-ODD IDENTIFIER\nInput q to quit\n-----------------------")

#While loop to keep asking
while True:
    try:
        x = input("Give me the number: ") 
        if x == "q":
            quit() #'q' terminates the program
        elif x == "":
            print("Looks like empty input!") #identify empty input
        elif x == " ":
            print("That was space, not a number!") #identify space
        elif int(x) == 0:
            print("Invalid Input!") #identify 0
        elif int(x)%2 == 0:
            print("That was an even number pal!") #identify even numbers
        elif int(x)%2 == 1:
            print("That was an odd number pal!") #identify odd numbers
    except:
        print("I don't know what that was!") #for other unknown inputs
        
