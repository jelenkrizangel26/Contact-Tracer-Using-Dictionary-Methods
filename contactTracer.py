# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# What do you want to do? (1-3): 3
# Exit? n

import time, sys

border = ("\n\33[34m**********************************************************************\33[0m\n")
starts ="\n\t              \33[3m\33[32mStarting!\33[0m"

def typePrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def intro():
    typePrint("\n\t \33[1m\33[32mGood day, Welcome to Krizzy's Contact Tracer!\33[0m\n")
    time.sleep(1)
    typePrint("\33[3m           Where you can find and add your details.\33[0m\n")
    time.sleep(1)

def menu():
    print(border)
    typePrint("Instruction: Pick a number from 1 to 3 to tell what you want to do.")
    time.sleep(1)
    list = ["\n1 -> Add an item","2 -> Search","3 -> Exit (y/n)"]
    print(list[0])
    print(list[1])
    print(list[2])

def start():
    while True:
        print(border)
        user = input("What do you want to do? (1-3): ")
        if user == '1':
            print(border)
            print(starts)
            print("Enter your details:\n")
            name = input("Full name: "),
            age = input("Age: "),
            add = input("Adress: " ),
            num = input("Phone Number: ")
            #make the dictionary
            user1 = {
                "Fullname": name,
                "Age": age,
                "Address": add,
                "Phone Number": num
            }

            dict.update(user1)
            print("\n\t              \33[1m\33[3m\33[32mYour info has been saved!\33[0m")
            
        elif user == '2':
            ask = input("Type the full name here: ")
            if ask in user1:
                print("\n\t              \33[1m\33[3m\33[32mExisting!\33[0m")
                for key, value in user1.items():
                    print(key, ":", value)
            else:
                print("\t\33[35m\33[1m        Data cannot be found. Try checking your spelling and captilization!\33[0m")


intro()
menu()
start()