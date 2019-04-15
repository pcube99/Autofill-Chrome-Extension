from application import app
import unittest

# python -m unittest test_app
class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'

    def test_login(self):
        rv = self.app.get('/login?email=pan@p.com&password=123456')
        self.assertEqual(rv.status, '200 OK')

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')

    def test_signup(self):
        rv = self.app.get('/signup')
        self.assertEqual(rv.status, '200 OK')

    def test_help(self):
        rv = self.app.get('/help')
        self.assertEqual(rv.status, '200 OK')

    def test_details(self):
        rv = self.app.get('/details')
        self.assertEqual(rv.status, '500 INTERNAL SERVER ERROR')
    
    def test_autofill(self):
        rv = self.app.get('/autofill?url=https://www.github.com')
        self.assertEqual(rv.status, '500 INTERNAL SERVER ERROR')
    
    def test_autoupdate(self):
        rv = self.app.get('/autoupdate')
        self.assertEqual(rv.status, '500 INTERNAL SERVER ERROR')

    
    

