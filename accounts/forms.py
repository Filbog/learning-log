from django import forms
from django.contrib.auth.forms import PasswordResetForm

# for email field during registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email


email_label = "Enter your email address below, and we'll email instructions for setting a new one."


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=email_label, max_length=254, required=True)
