from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UserAccountTests(TestCase):
    
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'username', 'firstname', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.username, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertEqual(super_user.password, 'password')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)

        self.assertEqual(str(super_user), 'username')