from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import SignupForm


class SignUp(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
