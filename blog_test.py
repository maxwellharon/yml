import unittest
from personalblog.models import User
from personalblog.models import Post
# from personalblog.forms  import RegistrationForm
from personalblog import db

# class TestRegistrationModel(unittest.TestCase):
#     def setUp(self):
#         '''
#         Set up method before each test case
# `       '''
#         self.registration = registration(username = "Emilly", email='Emillyoyolo@gmail.com' ,password =  'pass' , confirm_password = 'pass' , submit = 'submit')
#     def test_whether_username_registers(self):
#         self.assertEqual(self.registration.email, 'Emillyoyolo@gmail.com')


class TestUserModel(unittest.TestCase):

    '''
    This is a test class that checks whether our Registration form is working correctly
    '''

    def setUp(self):
        '''
        Set up method before each test case
`       '''
        self.user1 = User(username="admin", email="admin@gmail.com",password='1234',image_file="img/new.jpg" )
    def test_whether_instantiation_is_correct(self):
        self.assertEqual(self.user1.username, 'admin')

    def test_whether_email_works(self):
        self.assertEqual(self.user1.email, 'admin@gmail.com')

    def test_whether_password_works(self):
        self.assertEqual(self.user1.password, '1234')

    def test_whether_image_file_registers(self):
        self.assertEqual(self.user1.image_file, 'img/new.jpg')



    # def test_user_is_saved_in_database(self):
    #     db.create.all()
    #     db.session.add(self.user1)
    #     db.session.commit()
    #     users = User.query.all()
    #     self.assertTrue(length(users)>0)

class TestPostModel(unittest.TestCase):
    def setUp(self):
        '''
    Set up method before each TestCase
        '''

        self.user2 = Post(id = "1" , title = "Max" , content ="Max_I_am")
    def test_whether_content_work(self):
        self.assertEqual(self.user2.content, 'Max_I_am')

    def test_whether_title_work(self):
        self.assertEqual(self.user2.title, 'Max')


    def test_whether_id_works(self):
        self.assertEqual(self.user2.id, '1')



if __name__ == '__main__':
    unittest.main(verbosity=2)
