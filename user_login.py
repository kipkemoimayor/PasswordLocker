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
