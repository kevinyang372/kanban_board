import os
import unittest
from project import db, app, ma

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):
 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        self.assertEqual(app.debug, False)
 
    def tearDown(self):
        pass
       
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_calendar_page(self):
        response = self.app.get('/calendar', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_form_update(self):
        response = self.app.post(
          '/form_update',
          data = dict(taskname="test", completedate="2019-03-15", taskcategory="Doing"),
          follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_move_task(self):
        self.test_form_update()
        response = self.app.get('/move_task/1/Done', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        self.test_form_update()
        response = self.app.post('/update_date/1/2019-03-24', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        self.test_form_update()
        response = self.app.get('/delete_task/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()