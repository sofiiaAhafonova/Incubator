from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Profile
from .forms import UserForm, ProfileForm
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = Profile


class ProfileUpdateView(UpdateView):
    template_name = 'accounts/edit_profile.html'
    form_class = ProfileForm
    model = Profile

    def get_success_url(self):
        return reverse_lazy('profile', kwargs = {'pk': self.request.user.profile.id})


    def post(self , request , *args , **kwargs):
        self.object = self.get_object()
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = self.get_form()
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return self.form_valid(profile_form)
        else:
            return self.form_invalid(profile_form)

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = UserForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserForm(instance=self.request.user)
        return context