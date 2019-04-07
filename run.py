#!/usr/bin/env python3.6
from user_login import User
import random
from user_login import Password

def register(username,password,accountName):
    user_details=User(username,password,accountName)
    return user_details
def save_user(user_login):
    user_login.register()

'''
Function to delete Account info
'''
# def deletepassword(username,password,email):
#     user_details=User(username,password,email)
#     return user_details


def delete_account(user_login):
    user_login.delete_password()

"""
Display contacts
"""
def display_passwords():
    return User.display_user();


#Function to search password on specific Accounts

def search_accountPassword(number):
    return User.find_by_accountName(number);

def check_if_accountExist(number):
    return User.account_exist(number)

'''
This a function to generate random password
'''
def random_password(limit):
    password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!)"
    ran=len(password)
    hold=''
    for i in range(0,limit):
        all=password[random.randint(0,ran)]
        hold=hold+all
    return hold

def main():
        print("**********\n***********\n********")
        print("Welcome to password Locker Saves you password and hutsle of forgeting them")
        print("Please Register\n Enter your userName")
        name=input()
        print("chose g-generate password or m- to make your own password ")
        short_codes=input().lower()
        if short_codes=="g":
            print("Enter the length you would like you password to have recomendation:)5")
            limit=int(input())
            print('\n')
            print("**"*15)
            password=random_password(limit)
            print("Your password is "+password)
            print("**"*15)
        else:
            print("Enter your password")
            password=input()
        thisAccout="pass"
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
                print("These are short keys to help you navigate through\n cp- save new password dc-- display all passwords fa-- find a specific account password  dl-- delete password ex-- exit this application")
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
                        print("--"*40)
                        print("Account Name \t  Username\t password")
                        print("_"*60)
                        for account in display_passwords():
                            print(f"{account.username} \t {account.password}............{account.email}")
                            print("\n")
                        print("--"*40)
                    else:
                        print("\n")
                        print("It seems you have not Accounts yet")
                elif short_codes=="fa":
                    print("Enter Account name")
                    search_pass=input();
                    if check_if_accountExist(search_pass):
                        searchP=search_accountPassword(search_pass)
                        print("\n")
                        print("Account Match ------1")
                        print("Username\t password")
                        print("__"*20)
                        print(f"{searchP.password}...\t{searchP.email}")
                        print("--"*20)
                        print("\n")
                    else:
                        print("That Account does not exist Please Try again")
                        print("--"*20)
                        print("\n")

                elif short_codes=="dl":
                    print("Enter Account Name to be deleted")
                    delAccount=input();
                    if check_if_accountExist(delAccount):
                        for i in display_passwords():
                            if delAccount in i.username:
                                posi=display_passwords().index(i)
                        # delete_account(posi)
                        display_passwords().remove(display_passwords()[posi])

                        print(f"{delAccount} Account deleted succefully")
                        print("\n")
                    else:
                        print("Oh...an error occured That acount does not exist")






                elif(short_codes == "ex"):
                    print("are you sure about this \n yes or no")
                    sure=input().lower()
                    if sure=="no":
                        continue
                    else:
                        print("Existing...........\nBye!!!")
                        break
                else:
                    print("I didnt Get you would you mind using the short codes please")
        else:
            print("wrong usermame or password")
if __name__ == '__main__':
    main()
