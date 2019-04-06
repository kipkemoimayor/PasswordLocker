from user_login import User
import unittest
class UserTest(unittest.TestCase):
    def tearDown(self):
        '''
        This function ensures that each time the test runs it runs afresh without memory of preious details
        '''
        User.user_details=[]
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
    def test_save_user_details(self):
        self.user_details.register()
        test_userDetails=User("Test","user","gmail.com")
        test_userDetails.register()
        self.assertEqual(len(User.user_details),2)
    #delete password test
    def test_delete_password(self):
        self.user_details.register()
        test_userDetails=User("Test","user","gmail.com")
        test_userDetails.register()

        self.user_details.delete_password()
        self.assertEqual(len(User.user_details),1)
    #find user credetials by account name
    def test_find_by_accountName(self):
        self.user_details.register()
        test_userDetails=User("Test","user","gmail.com")
        test_userDetails.register()

        found_account=User.find_by_accountName("Test");
        self.assertEqual(found_account.username,test_userDetails.username)




if __name__ == '__main__':
    unittest.main()
