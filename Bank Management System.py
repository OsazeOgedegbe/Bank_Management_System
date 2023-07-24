#class BMS:
import os
from time import sleep
balance=0    
def openAccount():
    
    print("")
    print("Enter the following details to open an account")
    name=str(input("Enter your full name: "))
    age=int(input("Enter your age: "))
    if age<18:
        print("You are not eligible to open an account")
        print("Exiting the program....")
        return age
    else:
        savcurr=int(input("For a Savings account, Enter 1 :: For a Current account, Enter 2: "))
        if savcurr==1:
            print("")
            print("You have successfully opened a Savings account")
            print("CUSTOMER DETAILS:")
            print("NAME: ",name)
            print("AGE: ",age)
            print("BALANCE: #",balance)

        elif savcurr==2:
            print("")
            print("You have successfully opened a Current account")
            print("CUSTOMER DETAILS:")
            print("NAME: ",name)
            print("AGE: ",age)
            print("BALANCE: #",balance)

        else:
            print("")
            print("Enter a valid option for savings or current account")

        mainMenu=input("Press Enter to go back to the main menu")
        os.system('cls')
        return name


def deposit():

    print("")
    deposit=int(input("Enter an amount you'll like to deposit: "))
    newBalance=balance+deposit
    print("You have successfully deposited #",deposit,"into your account")

    mainMenu=input("Press Enter to go back to the main menu")
    os.system('cls')
    return newBalance



def withdraw():

    print("")
    withdraw=int(input("Enter an amount you'll like to withdraw: "))
    
    if withdraw>balance:
        print("Insufficient Funds")
        newBALANCE=balance
    else:
        newBALANCE=balance-withdraw
        print("You have successfully withdrawn #",withdraw,"from your account")
        

    mainMenu=input("Press Enter to go back to the main menu")
    os.system('cls')
    return newBALANCE
    


def viewBalance():

    print("")
    print("Account Name:",name_OR_age)
    print("Your current balance is #",balance)

    mainMenu=input("Press Enter to go back to the main menu")
    os.system('cls')

    

done=False
print("Welcome to the Bank Management System")
while done!=True:
    print("")
    print("MAIN MENU")
    print("1. Open an account")
    print("2. View Balance")
    print("3. Withdraw")
    print("4. Deposit")
    print("5. Exit")
    option=int(input("Pick an option to carry out the action: "))

    if option==1:
        name_OR_age=openAccount()
        if isinstance(name_OR_age,int):
            sleep(4)
            done=True


    elif option==2:
        if 'name_OR_age' in locals():
            viewBalance()
        else:
            print("You don't have an account!")
            print("Open an account first")
            mainMenu=input("Press Enter to go back to the main menu")
            os.system('cls')
        

    elif option==3:
        if 'name_OR_age' in locals():
            balance=withdraw()
        else:
            print("You don't have an account!")
            print("Open an account first")
            mainMenu=input("Press Enter to go back to the main menu")
            os.system('cls')
        

    elif option==4:
        if 'name_OR_age' in locals():
            balance=deposit()
        else:
            print("You don't have an account!")
            print("Open an account first")
            mainMenu=input("Press Enter to go back to the main menu")
            os.system('cls')
            

    elif option==5:
        print("You have successfully exited the system")
        done=True

        
    else:
        print("Select a valid option")

    
    
    
