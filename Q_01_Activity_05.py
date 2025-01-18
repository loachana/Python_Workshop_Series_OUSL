#18/1/2025
#This is the code for activity 5 of python workshop @ OUSL
#All rights reserved 


while True:
    try:
        q=input("the number: ")
        
    except:
        print("invalid")

    if q.isdigit():
        x = [i for i in range(1,11)]
        print(x)

        y = [q for i in range(1,11)]
        print(y)

        multi = [x[r]*y[r] for r in range(0,10)]
        print(multi)

        for d in range(0,10):
            #print(x[d],'x',y[d],'-->',multi[d])
            print(f"{x[d]}x{y[d]}-->{multi[d]}")


'''
while True:
    number = int(input("---"))

    if number == 1:
        break

'''
