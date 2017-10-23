from django.test import TestCase
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from user.templatetags.user_tags import allowed_age, bizzfuzz
from user.models import User


class HomePageTest(TestCase):
    def test_create_user(self):
        self.assertFalse(User.objects.all().exists())
        response = self.client.post(
            reverse_lazy('user:create'), {
                'username': 'admin',
                'birth_day': '1993-10-10',
                "password1": "sadfasf23e1e1",
                "password2": "sadfasf23e1e1"
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(1, User.objects.count())

    def test_update_user_get_200(self):
        user = User.objects.create(**{
                'username': 'admin',
                'birth_day': '1993-10-10',
                "password": "randompassword",
            })
        response = self.client.get(reverse_lazy('user:edit', args=(user.username,)))
        self.assertEqual(response.status_code, 200)

    def test_bizzfuzz_tag(self):
        dataset = [
            (40, 'Fuzz'),
            (66, 'Bizz'),
            (30, 'BizzFuzz'),
        ]
        for data in dataset:
            value, res = data
            self.assertEqual(bizzfuzz(value), res)

    def test_allowed_age_tag(self):
        user1 = User.objects.create(**{
                'username': 'max',
                'birth_day': '1993-10-10',
                "password": "randompassword",
            })
        user2 = User.objects.create(**{
                'username': 'alex',
                'birth_day': '2010-10-10',
                "password": "randompassword",
            })
        user1.refresh_from_db()
        user2.refresh_from_db()
        self.assertEqual(allowed_age(user1), _("allowed"))
        self.assertEqual(allowed_age(user2), _("blocked"))
