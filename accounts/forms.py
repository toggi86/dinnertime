from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', required=True)
    email_confirm = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'email_confirm', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('email_confirm')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with email {} already exists".format(email))
        if email_confirm != email:
            raise forms.ValidationError("Emails don't match")
