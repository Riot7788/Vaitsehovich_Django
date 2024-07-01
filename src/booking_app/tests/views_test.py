from django.test import TestCase, Client
from booking_app.models import User


class TestUserView(TestCase):

    def test_user_list_view(self):
        first_name = "TestName"
        last_name = "TestLastName"
        age = 30
        sex = "m"
        User.objects.create(first_name=first_name,
                            last_name=last_name,
                            age=age,
                            sex=sex)
        path = "/booking/create_user"
        client = Client()
        response = client.get(path=path)
        # self.assertIn('create_user', response.context)
        user = response.context["create_user"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(user), 1)
        self.assertEqual(user[0].first_name, first_name)
        self.assertEqual(user[0].last_name, last_name)
        self.assertEqual(user[0].age, age)
        self.assertEqual(user[0].sex, sex)
