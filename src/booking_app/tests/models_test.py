from django.test import TestCase
from booking_app.models import User

class TestUserModels(TestCase):

    def test_create_user(self):
        first_name = "TestName"
        last_name = "TestLastName"
        age = 25
        sex = "m"
        user = User.objects.create(first_name=first_name,
                            last_name=last_name,
                            age=age,
                            sex=sex)
        import pdb;pdb.set_trace()
        self.assertEqual(user.id, 1)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.first_name, last_name)
        self.assertEqual(user.first_name, age)
        self.assertEqual(user.first_name, sex)
