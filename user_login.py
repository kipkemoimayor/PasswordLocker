import random
class User():
    """
        created an empty list to hold users info
    """
    user_details=[]; #empty

    def __init__(self, username,password,email):
        self.username=username
        self.password=password
        self.email=email
    def register(self):
        User.user_details.append(self)
    def delete_password(self):
        User.user_details.remove(self)

    @classmethod
    def find_by_accountName(cls,number):
        for user in cls.user_details:
            if user.username==number:
                return user
    @classmethod
    def account_exist(cls,number):
        for user in cls.user_details:
            if user.username==number:
                return True;
        return False

    @classmethod
    def display_user(cls):
        return cls.user_details

class Password():
    def __init__(self,ranPassword):
         self.ranPassword=ranPassword
    def generatePassword():
        password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!)"
        return password
