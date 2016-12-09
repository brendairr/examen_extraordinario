from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
from views import login


# Create your tests here.
class LoginTest(TestCase):

    def test_login(self):
        response = self.client.get("/login/")
        self.assertTemplateUsed(response, 'login.html')


    def test_login_sesion(self):
            c = Client()
            response = c.post('/login', {'username': 'admin', 'password': 'root1234'})
            self.assertEqual(response.status_code, 301)

    def test_login_returns_correct_html(self):
        request = HttpRequest()
        response = login(request)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_status_code(self):
        request = HttpRequest()
        response = login(request)
        self.assertEqual(response.status_code, 200)
