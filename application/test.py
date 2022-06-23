from app import app
import unittest

from application.routes import Routes 

class FlaskTestCase(unittest.TestCase):

    id_num = Routes().id_num
    print(id_num)
    
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_add(self):
        tester = app.test_client(self)
        response = tester.get('/add', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_update(self):
        id_num = self.id_num 
        tester = app.test_client(self)
        response = tester.get(f'/movies_update/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_delete(self):
        id_num = self.id_num
        tester = app.test_client(self)
        response = tester.get(f'/delete/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_add_review(self):
        id_num = self.id_num
        tester = app.test_client(self)
        response = tester.get(f'/add_review/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_reviews(self):
        id_num = self.id_num
        tester = app.test_client(self)
        response = tester.get(f'/reviews/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    
if __name__ == '__main__':
    unittest.main()