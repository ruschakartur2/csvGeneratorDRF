from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from users.forms import UserForm


class CreateUser(CreateView):
    template_name = 'registration/register.html'
    success_url = '/'
    form_class = UserForm
    queryset = get_user_model().objects.all()

    def is_valid(self, form):
        user = get_user_model().objects.create_user(form.cleaned_data['username'],
                                                    form.cleaned_data['password1'])
