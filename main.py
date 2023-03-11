import pandas as pd
import os
from artwork import logo
from IPython.display import clear_output

def register_User():
    """
    Handles user registration and writes to a csv file
    """
    print("To register, please enter your info:")
    email = input("E-mail: ")
    password = input("Password: ")
    password2 = input("Re-type password: ")
    
    clear_output()
    
    try:
        df = pd.read_csv("users.csv")
        if email in df["Email"].values:
            clear_screen()
            print("This account is already registered in the database. Try logging instead.\n")
            return
    except FileNotFoundError:
        pass
        
    if password == password2:
        df = pd.DataFrame({"Email": [email], "Password": [password]})
        df.to_csv("users.csv", mode="a", header=not os.path.isfile("users.csv"), index=False)
        clear_screen()
        print("You are now registered. Welcome!")
    else:
        print("Password's don't match. Please try again")

def login_User():
    """Asks for user login info

    Returns:
        True to login or False if incorrect 
    """
    print("To login, please enter your credentials info")
    email = input("Email: ")
    password = input("Password: ")

    clear_output()
    try: 
        df = pd.read_csv("users.csv")
        if ((df["Email"] == email) & (df["Password"] == password)).any():
            clear_screen()
            print("\nYou are now logged in!")
            return True
    except FileNotFoundError:
        pass
    
    clear_screen()
    print("User account not found in the database. Please make sure you register first.\n")
    return False

def clear_screen():
    """
    Clears the terminal screen regardless of windows/linux/mac
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Vars for main loop
active = True
logged_in = False
df = pd.read_csv("users.csv")

# Main loop
while active:
    while logged_in:
        print("\n1. Print Database\n2. Logout\n3. Quit")
        choice = input("What would you like to do? ")
        if choice == "1":                               # Prints database
            clear_screen()
            print("\nPrinting database...\n")
            print(df)
            print("\n")
        elif choice == "2":                             # Logout
            logged_in = False
            clear_screen()
            print("You are now logged out. Goodbye!\n") 
        elif choice == "3":                             # Quit  
            active = False
            print("Have a great day!")
            exit()

    print(logo)
    print("1. Login\n2. Register\n3. Quit")
    choice = input("What would you like to do? ")
    

    clear_output()

    if choice == "1" and not logged_in:             # Login
        logged_in = login_User()
    elif choice == "2" and not logged_in:           # Register
        register_User()
    elif choice == "3":                             # Quit
        active = False
        print("Have a great day!")
    else:
        clear_screen()
        print("\nPlease try again and pick a number listed below.\n")
