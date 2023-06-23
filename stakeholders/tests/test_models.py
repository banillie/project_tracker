from django.conf import settings
from django.test import TestCase
from test_factory.factories import StakeholderFactory

from stakeholders.models import StakeholderOrg, DFTGroup

User = settings.AUTH_USER_MODEL

class StakeholderModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.stakeholder = StakeholderFactory()

    def test_str_representation(self):
        stakeholder = StakeholderFactory(first_name='John', last_name='Doe')
        self.assertEqual(str(stakeholder), 'John Doe')

    def test_get_absolute_url(self):
        expected_url = f'/stakeholders/{self.stakeholder.slug}/'
        self.assertEqual(self.stakeholder.get_absolute_url(), expected_url)

    def test_get_update_url(self):
        expected_url = f'/stakeholders/{self.stakeholder.slug}/update/'
        self.assertEqual(self.stakeholder.get_update_url(), expected_url)

    def test_save_method_with_my_dft_url(self):
        stakeholder = StakeholderFactory(organisation__name='DfT(c)', my_dft_url=None)
        stakeholder.save()
        expected_url = f'https://intranet.dft.gov.uk/users/{stakeholder.slug}'
        self.assertEqual(stakeholder.my_dft_url, expected_url)

    def test_save_method_without_my_dft_url(self):
        stakeholder = StakeholderFactory(organisation__name='Some Org', my_dft_url=None)
        stakeholder.save()
        self.assertIsNone(stakeholder.my_dft_url)

    # # not working
    # def test_user_field(self):
    #     self.assertIsInstance(self.stakeholder.user, User)

    def test_fields(self):
        self.assertIsInstance(self.stakeholder.first_name, str)
        self.assertIsInstance(self.stakeholder.last_name, str)
        self.assertIsInstance(self.stakeholder.slug, str)
        self.assertIsInstance(self.stakeholder.last_name, str)
        self.assertIsInstance(self.stakeholder.organisation, StakeholderOrg)
        self.assertIsInstance(self.stakeholder.group, str)
        self.assertIsInstance(self.stakeholder.dft_group, DFTGroup)
        self.assertIsInstance(self.stakeholder.team, str)
        self.assertIsInstance(self.stakeholder.role, str)
        self.assertIsInstance(self.stakeholder.tele_no, str)
        self.assertIsInstance(self.stakeholder.live, bool)
        self.assertIsInstance(self.stakeholder.my_dft_url, str)
