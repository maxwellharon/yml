import unittest
from personalblog.models import User
from personalblog.models import Post
from personalblog.forms import RegistrationForm
from personalblog.forms import LoginForm
from personalblog.forms import UpdateAccountForm
from personalblog.forms import PostForm

# class TestUserModel(unittest.Testcase):
#     def test(self):
#         pass
class TestUserModel(unittest.TestCase):
    def setUp(self):
        '''
        Setup method before each testcase
        '''
        self.user = User(id ="1" , username = "Max" , email= "maxwellharon@gmail.com" )
    def id_test(self):
        self.assertTrue(self.user.id, '1')

    def username_Test(self):
        self.assertTrue(self.user.username, 'Max')

    def email_test(self):
        self.assertTrue(self.user.email, 'maxwellharon@gmail.com')





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


class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        '''
        Set up method before each TestCase
        '''

        self.registration = RegistrationForm(username="Max",email="maxwellharon@gmail.com",password="1234",confirm_password="1234",submit="signup")
    def registration_Username(self):
        self.assertEqual(self.registration.username, 'Max')


    def registration_Email(self):
        self.assertEqual(self.registration.email, 'maxwellharon@gmail.com')


    def registration_Password(self):
        self.assertEqual(self.registration.password, '1234')


    def registration_confirm_password(self):
        self.assertEqual(self.registration.confirm_password, '1234')


    def registration_submit(self):
        self.assertEqual(self.registration.submit, 'signup')


class LoginForm(unittest.TestCase):
    def setUp(self):
        '''
        Setup method before each testcase
        '''
        self.login = LoginForm(email= "maxwellharon@gmail.com" ,password = "1234" , submit = "Ok")
    def login_email(self):
        self.assertEqual(self.login.email, 'maxwellharon@gmail.com')
        # result = self.login.maxwellharon@gmail.com
        # self.assertEqual(maxwellharon@gmail.com, result)



    def login_password(self):
        # result = self.login_password, '1234'
        # self.assertCountEqual(1234, result)
        self.assertEqual(self.loginForm.password, '1234')


    def login_submit(self):
        # result = self.login_submit, 'ok'
        # self.assertRaises(ok, result)
        self.assertEqual(self.loginForm.submit, 'ok')


class UpdateAccountForm(unittest.TestCase):
    def setUp(self):
        '''
        Setup method before each testcase
        '''
        self.update = UpdateAccountForm(username="maxwell",email="user@gmail.com", submit="ok")
    def username_Test(self):
        # result = self.username_Test, 'maxwell'
        # self.assertRaises(Maxwell, result)
        self.assertEqual(self.update.username, 'maxwell')
        # pass

    def email_test_Update(self):
        # result = self.email_test, 'user@gmail.com'
        # self.assertTrue(user@gmail.com, result)
        self.assertEqual(self.update.email, 'user@gmail.com')
        # pass

    def SubmitField_Test(self):
        # result = self.SubmitField_Test, 'ok'
        # self.assertTrue(ok, result)
        self.assertEqual(self.update.submit, 'ok')
        # pass

class PostForm(unittest.TestCase):
    def setUp(self):
        '''
        Setup method before each testcase
        '''
        self.post = PostForm(title = "RegiBiz",content = "Registration of different businesses", submit = "post" )
    def title_Test(self):
        # result = self.title_Test, 'RegiBiz'
        # self.assertTrue(RegiBiz, result)
        self.assertEqual(self.post.title, 'RegiBiz')
        # pass

    def content_test(self):
        # result = self.content_Test, 'Registration of different businesses'
        # self.assertTrue(Registration of different businesses, result)
        self.assertEqual(self.post.content, 'Registration of different businesses')
        # pass


    def submit_Test(self):
        # result = self.submit_Test, 'post'
        # self.assertTrue(post, result)
        self.assertEqual(self.post.content, 'Registration of different businesses')
        # pass


class SearchForm(unittest.TestCase):
    def setUp(self):
        '''
        Setup method before each testcase
        '''

        self.search = SearchForm(search="post",submit="search")
    def search_Test(self):
        # result = self.search_Test, 'post'
        # self.assertTrue(post, result)
        self.assertEqual(self.search.search, 'post')
        # pass

    def submitSearch_Test(self):
        # result = self.submitSearch_Test, 'search'
        # self.assertTrue(search, result)
        self.assertEqual(self.search.post, 'post')
        # pass

    # def fname(arg):
    #     pass










# if __name__ == '__main__':
#     unittest.main()
