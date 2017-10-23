import csv

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from user.forms import UserCreateForm, UserEditForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import User
from user.templatetags.user_tags import allowed_age, bizzfuzz


class BaseUserView:
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserListView(ListView):
    model = User


class UserDetailView(BaseUserView, DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class UserEdit(BaseUserView, UpdateView):
    model = User
    form_class = UserEditForm


class UserDelete(BaseUserView, DeleteView):
    model = User
    success_url = reverse_lazy('user:list')


def export_user_list_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_list.csv"'
    writer = csv.writer(response)

    header = ["Username", "Birthday", "Eligible", "Random Number", "BizzFuzz"]
    writer.writerow(header)

    for user in User.objects.all():
        writer.writerow([
            user.username,
            user.birth_day,
            allowed_age(user),
            user.random_number,
            bizzfuzz(user.random_number)
        ])
    return response