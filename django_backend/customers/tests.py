from django.test import TestCase, Client


class CustomerAppTest(TestCase):

    client = Client()

    def test_smoke_test(self):
        response = self.client.get("/admin/login/")
        self.assertIn("<title>Log in | Django site admin</title>",
                      response.content.decode(), response.content.decode())
        self.client.login(username= "hr", password= "UploadExcel@123")

    def test_create_customer(self):
        response = self.client.post(
            "/api/create_customer", {'name': 'charu', 'age': 12})
        self.assertEqual(200, response.status_code, 'POst didint go properly.')
