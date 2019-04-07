import random
def randomp(limit):
    password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!)"
    ran=len(password)
    hold=''
    for i in range(0,limit):
        all=password[random.randint(0,ran)]
        hold=hold+all
    print(hold)
randomp(int(input()))
