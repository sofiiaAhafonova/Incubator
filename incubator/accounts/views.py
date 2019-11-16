from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, FormView
from .models import Profile

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = Profile


class ProfileUpdateView(FormView):
    model = Profile
    template_name = 'accounts/update_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context