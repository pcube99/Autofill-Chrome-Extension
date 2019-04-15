from application import app
import unittest

# python -m unittest test_app
class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main(self):
        rv = self.app.get('afss.herokuapp.com/')
        assert rv.status == '200 OK'

    def test_login(self):
        rv = self.app.get('afss.herokuapp.com/login?email=pa@.com&password=123456')
        self.assertEqual(rv.status, '200 OK')

    def test_login1(self):
        rv = self.app.get('afss.herokuapp.com/login?email=pa&password=1234')
        self.assertEqual(rv.status, 'Invalid')
	
	
    def test_404(self):
        rv = self.app.get('afss.herokuapp.com/other')
        self.assertEqual(rv.status, '404 NOT FOUND')

    def test_signup(self):
        rv = self.app.get('afss.herokuapp.com/signup')
        self.assertEqual(rv.status, '200 OK')

    def test_help(self):
        rv = self.app.get('afss.herokuapp.com/help')
        self.assertEqual(rv.status, '200 OK')

    def test_details(self):
        rv = self.app.get('afss.herokuapp.com/details')
        self.assertEqual(rv.status, '500 INTERNAL SERVER ERROR')
    
    def test_autofill(self):
        rv = self.app.get('afss.herokuapp.com/autofill?url=https://www.github.com')
        self.assertEqual(rv.status, '500 INTERNAL SERVER ERROR')
    
    def test_autoupdate(self):
        rv = self.app.get('afss.herokuapp.com/autoupdate')
        self.assertEqual(rv.status, '500 INTERNAL SERVER ERROR')

    def test_logout(self):
        rv = self.app.get('afss.herokuapp.com/logout')
        self.assertEqual(rv.status, '302 FOUND')

    def test_loginwebsite(self):
        rv = self.app.get('afss.herokuapp.com/login_website')
        self.assertEqual(rv.status, '200 OK')    
