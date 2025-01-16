#16/1/2025
#This is the code for Q2 in activity 4 of python workshop @ OUSL
#All rights reserved 

#>> We use while toop to keep asking integers from the user.
#>> We also use Try-Except block to prevent the user to enter invalid input.
#>> Inside the loop, We use If statement to classify the integer given by the user.

#The head
print("THE THREE FIVE FACTOR IDENTIFIER\nInput 0 to stop\n--------------------------------")

#While loop to keep asking
while True:
    try:
        x = input("Give me the number: ") 

        
        if x == "":
            print("Looks like empty input!") #identify empty input
        elif x == " ":
            print("That was space, not a number!") #identify space
        elif int(x) == 0:
            break #0 breaks the program
        elif int(x)%3 == 0 and int(x)%5 == 0:
            print(x,"is devisible by both 3 and 5") #identify numbers by 3,5 
        elif int(x)%3 == 0:
            print(x, "is devisible by 3") #identify numbers by 3
        elif int(x)%5 == 0:
            print(x, "is devisible by 5") #identify numbers by 5
        else:
            print(x,"is devisible by neither both 3 and 5") #Numbers neither 3,5
    except:
        print("I don't know what that was!") #for other unknown inputs
        
