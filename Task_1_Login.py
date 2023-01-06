import re
import pandas
import os
from replit import clear


def register():
    email_pattern = "^[a-zA-Z][a-zA-Z_0-9-.]+[@][a-zA-Z]+[.][a-zA-Z]{2,3}"
    email_set = False
    while not email_set:
        email_id = input("Enter E-mail ID:")
        user_data = pandas.read_csv("User_Login_Details.txt")
        email_existing = False
        for u_mail in user_data['email_id']:
            if u_mail == email_id:
                print("E-mail_ID already exists. Kindly register using a different E-mail_ID\n")
                email_existing = True
        if not email_existing:
            x = re.fullmatch(email_pattern, email_id)
            if x:
                print("You Have Entered a valid Email_ID!\n")
                email_set = True
                password_pattern = "(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{5,12}"
                password_set = False
                while not password_set:
                    password = input("Enter Password:")
                    y = re.fullmatch(password_pattern, password)
                    if y:
                        password_set = True
                        print("Password Validated")
                        return email_id, password
                    else:
                        print("You have Entered an Invalid Password")
                        if not re.fullmatch("[a-zA-Z0-9!@#$%^&*]{5,12}", password):
                            print("The length of password should be minimum 5 and maximum 16 characters")
                        elif not re.match("(?=.*[A-Z])", password):
                            print("Password should contain at least one upper case character")
                        elif not re.match("(?=.*[a-z])", password):
                            print("Password should contain at least one lower case character")
                        elif not re.match("(?=.*[0-9])", password):
                            print("Password should contain at least one digit")
                        elif not re.match("(?=.*[!@#$%^&*])", password):
                            print("Password should contain at least one special character")
            else:
                print("\nInvalid Email ID!\nInstructions:\n* First Letter of E-mail ID should not be a "
                      "Numeric or special Character\n* Should have \"@\" followed by \".\" but should not be immediate "
                      "next to \"@\"\n")


def login(email):
    global u_password
    u_password = ""
    user_data = pandas.read_csv("User_Login_Details.txt")
    for (index, rows) in user_data.iterrows():
        if rows.email_id == email:
            u_password = rows.password
    if u_password == "":
        print("Your email_ID has not been registered. Kindly register to login.")
    else:
        retry = False
        while not retry:
            login_password = input("Enter your password:\n")
            if login_password == u_password:
                print("Login Successful")
                retry = True
            else:
                decision = input("Wrong Password\nSelect(1/2/3) to proceed:\n1. Forgot Password(Retrieve)\n2. Reset "
                                 "Password\n3. Re-try\n")
                if decision == "1":
                    print("Your password is : ", u_password)
                    retry = True
                elif decision == "2":
                    new_password_valid = False
                    while not new_password_valid:
                        new_password = input("Enter your new Password:\n")
                        password_pattern = "(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{5,12}"
                        if re.fullmatch(password_pattern, new_password):
                            new_password_valid = True
                        else:
                            print("You have Entered an Invalid Password")
                            if not re.fullmatch("[a-zA-Z0-9!@#$%^&*]{5,12}", new_password):
                                print("The length of password should be minimum 5 and maximum 16 characters")
                            elif not re.match("(?=.*[A-Z])", new_password):
                                print("Password should contain at least one upper case character")
                            elif not re.match("(?=.*[a-z])", new_password):
                                print("Password should contain at least one lower case character")
                            elif not re.match("(?=.*[0-9])", new_password):
                                print("Password should contain at least one digit")
                            elif not re.match("(?=.*[!@#$%^&*])", new_password):
                                print("Password should contain at least one special character")

                    with open("User_Login_Details.txt", mode="r+") as filer:
                        data = filer.readlines()
                        filer.truncate()
                    with open("User_Login_Details.txt", mode="w") as filew:
                        for i in data:
                            if i.find(email) == -1:
                                filew.write(i)
                            else:
                                filew.write(email+","+new_password+"\n")
                    print("Your password has been successfully changed\n")
                    retry = True
                elif decision == 3:
                    continue


while True:
    with open("User_Login_Details.txt", mode="a") as file:
        if os.path.getsize("User_Login_Details.txt") == 0:
            file.write("email_id,password\n")
    user_choice = input("\nWelcome User!\nKindly enter your choice:\n1.Register\n2.Login Account\n3.Exit\nPress 1/2/3\n")
    if user_choice == "1":
        clear()
        print("Registration")
        with open("User_Login_Details.txt", mode="a") as file:
            user_email, user_password = register()
            print("User Name: " + user_email + "\nPassword: " + user_password + "\n")
            file.write(user_email+","+user_password+"\n")
            print("Registration Successful\n")

    elif user_choice == "2":
        print("User Login")
        login_email = input("Enter your registered email ID:\n")
        login(login_email)

    elif user_choice == "3":
        print("Thank You!")
        exit()
