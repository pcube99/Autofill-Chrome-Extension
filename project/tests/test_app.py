from project.application import app
import unittest

# python -m unittest test_app
class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'Main' in rv.data
        #assert False

    def test_login(self):
        rv = self.app.get('/login?email=pan@p.com&password=123456')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, '5')

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')