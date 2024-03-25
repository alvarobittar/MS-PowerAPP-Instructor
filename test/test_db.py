import unittest
from app import app

class testdb(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.db = self.app.app_context().db
        self.db.drop_all()
        self.db.create_all()

    def tearDown(self):
        self.db.drop_all()
        self.app.testing = False
        self.app = None
        self.db = None
    
    def test_add_user(self):
        self.assertEqual(self.db.query(User).count(), 0)
        self.app.post('/add_user', data=dict(username='test', password='<PASSWORD>'), follow_redirects=True)
        self.assertEqual(self.db.query(User).count(), 1)
    
    