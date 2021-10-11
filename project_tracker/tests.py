import os
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password # django password_validation method


class ProjectTrackerConfigTest(TestCase):
    def test_secret_key_strength(self):
        # settings.SECRET_KEY
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak secret key {e.messages}'
            self.fail(msg)

