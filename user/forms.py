import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import extras
from django.utils.translation import ugettext_lazy as _



def get_current_year():
    return datetime.datetime.now().year


class UserEditForm(forms.ModelForm):
    birth_day = forms.DateField(
        label=_('Birth day'),
        widget=extras.SelectDateWidget(years=range(get_current_year(), 1900, -1)),
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'birth_day']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_day'].initial = self.instance.birth_day


class UserCreateForm(UserEditForm, UserCreationForm):
    pass