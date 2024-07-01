from django.test import TestCase, Client
from booking_app.models import User


class TestUserForm(TestCase):

    def test_user_form(self):
        first_name = "TestName"
        last_name = "TestLastName"
        age = 25
        sex = "m"
        # photo = "user_photo/user1.jpg"

        path = "/booking/create_user"
        client = Client()
        response = client.get(path=path,
                              data={
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "sex": sex,
                # "photo": photo
            })

        user = User.objects.get(id=1)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.age, age)
        self.assertEqual(user.sex, sex)
        # self.assertEqual(user.photo, photo)
