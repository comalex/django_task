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
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)