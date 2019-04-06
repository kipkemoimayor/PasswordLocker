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
