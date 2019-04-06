#!/usr/bin/env python3.6
from user_login import User

def register(username,password,accountName):
    user_details=User(username,password,accountName)
    return user_details
def save_user(user_login):
    user_login.register()
"""
Display contacts
"""
def display_passwords():
    return User.display_user();

def main():
        print("**********\n***********\n********")
        print("Welcome to password Locker Saves you password and hutsle of forgeting them")
        print("Please Register\n Enter your userName")
        name=input()
        print("Enter your password")
        password=input()
        print("Enter your Your email")
        email=input()
        thisAccout="PasswordLPlus"
        save_user(register(thisAccout,password,name))
        print("\n")
        print(f"Welcome {name}! Please Login ")
        print("Enter your username that you just created")
        vUser=input()
        print("enter your password ")
        vPassword=input()
        if vUser ==name and vPassword==password:
            print(f"Welcome to your dashboard {name}")
            while True:
                print("These are short keys to help you navigate through\n cp- save new password dc-- display all passwords dc-- find a specific account password  dl-- delete password ex-- exit this application")
                short_codes=input().lower()
                if short_codes=="cp":
                    print("-"*10)
                    print("Ready to create new password\n")
                    print(f"{name} Please enter the account name you need to be saved eg-Instagram | Facebook")
                    thisAccout=input();
                    print("Enter username")
                    username=input();
                    print("Enter the password make sure no one is watching")
                    password=input()
                    save_user(register(thisAccout,username,password))
                    print("\n")
                    print(f"{thisAccout} account details saved succefully")


                elif short_codes=="dc":
                    if display_passwords():
                        print(f"{name} This are all your passwords keep em save")
                        print("--"*20)
                        print("\n")
                        print("Account Name \t  Username\t password")
                        print("_"*90)
                        for account in display_passwords():
                            print(f"{account.username} \t {account.password}............{account.email}")
                            print("\n")
                        print("--"*20)
                    else:
                        print("\n")
                        print("It seems you have not Accounts yet")


                elif(short_codes == "ex"):
                    print("are you sure about this \n yes or no")
                    sure=input().lower()
                    if sure=="no":
                        continue
                    else:
                        break
        else:
            print("wrong usermame or password")
if __name__ == '__main__':
    main()
