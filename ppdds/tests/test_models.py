from django.test import TestCase

from ppdds.models import PPDD
from test_factory.factories import PPDDFactory

class PPDDModelTest(TestCase):
    def test_create_ppdd(self):
        ppdd = PPDDFactory()
        self.assertIsInstance(ppdd, PPDD)
        self.assertIsNotNone(ppdd.user)
        self.assertIsNotNone(ppdd.first_name)
        self.assertIsNotNone(ppdd.last_name)
        self.assertIsNotNone(ppdd.slug)
        self.assertIsNotNone(ppdd.team)
        self.assertIsNotNone(ppdd.division)
        self.assertIsNotNone(ppdd.role)
        self.assertIsNotNone(ppdd.tele_no)
        self.assertTrue(ppdd.live)

    def test_get_absolute_url(self):
        ppdd = PPDDFactory()
        url = ppdd.get_absolute_url()
        expected_url = f"/ppdds/{ppdd.slug}/"
        self.assertEqual(url, expected_url)
