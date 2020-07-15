from django.test import TestCase

from API.user.models.user import User


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            auth_id="123456789",
            username="test_user",
            avatar="a_url.png",
            avatar_cropped="a_url.png",
        )

    def test_user_is_created(self):
        user = User.objects.get(username="test_user")

        self.assertEqual(user.username, 'test_user')
