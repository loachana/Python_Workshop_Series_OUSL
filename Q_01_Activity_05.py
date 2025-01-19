#18/1/2025
#This is the code for activity 5 of python workshop @ OUSL
#All rights reserved 


while True:

    print("----------------\nTHE MATH TABLE\npress q to quit\n----------------")

    input_number = input("the number: ")

    if input_number == 'q'or input_number =='Q':
        break
    elif input_number.isdigit():
        one_to_ten_array = [i for i in range(1,11)]
        #print(one_to_ten_array)

        input_number_array = [int(input_number) for j in range(1,11)]
        #print(input_number_array)

        multiplication = [one_to_ten_array[k]*input_number_array[k] for k in range(0,10)]
        print(f"\nThe Array of Multiplication Table\n---------------------------------------------\n{multiplication}\n")


        for p in range(0,10):
            if p == 0:
                print("The Readable Math Table\n---------------------------------------------")
            print(f"{one_to_ten_array[p]} x {input_number_array[p]} = {multiplication[p]}\n")
            
    else:
        print("Invalid input! Please try again.")



    

