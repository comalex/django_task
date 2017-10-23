from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_task.miko.user.forms import UserCreateForm, UserEditForm
from django.urls import reverse_lazy

from .models import User


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