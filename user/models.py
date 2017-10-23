import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


def random_value():
    return random.randint(1, 100)


@python_2_unicode_compatible
class User(AbstractUser):
    birth_day = models.DateField(_("Birth day"), null=True, blank=True)
    random_number = models.PositiveIntegerField(default=random_value)

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'username': self.username})