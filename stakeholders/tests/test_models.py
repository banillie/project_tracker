from django.test import TestCase
from test_factory.factories import StakeholderFactory

class StakeholderModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.stakeholder = StakeholderFactory()

    def test_str_representation(self):
        # stakeholder = StakeholderFactory(first_name='John', last_name='Doe')
        self.assertEqual(self.stakeholder.first_name, 'John')

    def test_get_absolute_url(self):
        stakeholder = StakeholderFactory()
        expected_url = f'/stakeholders/{stakeholder.slug}/'
        self.assertEqual(stakeholder.get_absolute_url(), expected_url)

    def test_get_update_url(self):
        stakeholder = StakeholderFactory()
        expected_url = f'/stakeholders/{stakeholder.slug}/update/'
        self.assertEqual(stakeholder.get_update_url(), expected_url)

    def test_save_method_with_my_dft_url(self):
        stakeholder = StakeholderFactory(organisation__name='DfT(c)', my_dft_url=None)
        stakeholder.save()
        expected_url = f'https://intranet.dft.gov.uk/users/{stakeholder.slug}/'
        self.assertEqual(stakeholder.my_dft_url, expected_url)

    def test_save_method_without_my_dft_url(self):
        stakeholder = StakeholderFactory(organisation__name='Some Org', my_dft_url=None)
        stakeholder.save()
        self.assertIsNone(stakeholder.my_dft_url)
