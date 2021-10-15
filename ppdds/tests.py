from django.test import TestCase
from django.utils.text import slugify

from .models import PPDD
from .utils import slugify_instance_title


class PPDDTestCast(TestCase):
    def setUp(self):
        PPDD.objects.create(
            first_name='Jimmy',
            last_name='Jones'
        )

    def test_slug(self):
        obj = PPDD.objects.all().order_by("id").first()
        slug = obj.slug
        self.assertEqual(slug, 'jimmy-jones')
