#21/1/2025
#This is the answer for anctivity 7
#All rights reserved


#Creating book class
class book:
    #Initiating function 
    def __init__(self, title, author, year):
        self.title = title #Attribute
        self.author = author #Attribute
        self.year = year #Attribute

    #Creating a method to display attributes above
    def display_out(self):
        print(f"The Title: {self.title}\nThe Author: {self.author}\nPublished Year: {self.year}\n")

#Creating three objects
book_1 = book("Harry Potter", "J K Rowling", "2000")
book_2 = book("Secret Seven", "Enid Blyton", "1950")
book_3 = book("Power of Habit", "Charles Duhigg", "2012")

#Calling display_out function to print out
book_1.display_out()
book_2.display_out()
book_3.display_out()
