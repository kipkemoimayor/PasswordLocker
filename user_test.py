from user_login import User
import unittest
class UserTest(unittest.TestCase):
    def setUp(self):
        """
            This is a set up function that runs every time before each test clauses
        """
        #checks if there is data in our list
        self.user_details=User("collins24","ki154","coo@gmail.com")
    def test_init(self):
        self.assertEqual(self.user_details.username,"collins24")
        self.assertEqual(self.user_details.password,"ki154")
        self.assertEqual(self.user_details.email,"coo@gmail.com")
    def test_register(self):
        self.user_details.register();
        self.assertEqual(len(User.user_details),1)


if __name__ == '__main__':
    unittest.main()
