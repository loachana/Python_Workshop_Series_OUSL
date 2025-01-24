#21/1/2025
#This is in response to the Q2 of activity 6.
#All rights reserved.

#The function is defined 
def even_odd_inspector(num_guy):
    if num_guy%2 == 0:
        return "even"
    elif num_guy%2 == 1:
        return "odd"

#Recurring process
while True:
    try:
        input_number = input("Enter the number: ")
        input_number_int = int(input_number)
        result = even_odd_inspector(input_number_int)
        print(result)

    except:

        if input_number == "q" or input_number == "Q":
            break
        print("Enter valid number!")
        

    
