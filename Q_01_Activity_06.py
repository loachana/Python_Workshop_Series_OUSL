#21/1/2025
#This is in response to the Q1 of activity 6.
#All rights reserved

#The function is defined 
def summing_machine(num1, num2): #Take two arguments as num1, num2
    
    The_output = num1 + num2 #Summing process
    
    return(The_output) #returns the sum

#Testing
print(f"The sum of 42352525 and 23524334 are: {summing_machine(42352525,23524334)}\n")

#Further improvements
input1 = int(input("First number: "))
input2 = int(input("Second number: "))

print(f"The sum of {input1} and {input2} are {summing_machine(input1,input2)}")
