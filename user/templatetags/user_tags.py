from django import template
from django.utils.translation import ugettext_lazy as _
from django_task.miko.user.utils import calculate_age

register = template.Library()


@register.simple_tag
def allowed_age(user):
   if calculate_age(user.birth_day) > 13:
       return _("allowed")
   else:
       return _("blocked")



@register.filter
def bizzfuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'BizzFuzz'
    elif n % 3 == 0:
        return 'Bizz'
    elif n % 5 == 0:
        return 'Fuzz'
    else:
        return str(n)