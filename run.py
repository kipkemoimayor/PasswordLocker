#!/usr/bin/env python3.6
from user_login import User

def register(username,password,accountName):
    user_details=User(username,password,accountName)
    return user_details
def save_user(user_login):
    user_login.register()

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
        save_user(register(name,password,thisAccout))
        print("\n")
        print(f"Welcome {name}! Please Login ")
        print("Enter your username that you just created")
        vUser=input()
        print("enter your password ")
        vPassword=input()
        if vUser ==password and vPassword==password:
            print(f"Welcome to your dashboard {name}")
        else:
            print("wrong usermame or password")
if __name__ == '__main__':
    main()
