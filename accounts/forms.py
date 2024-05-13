from django import forms
from django.contrib.auth.forms import PasswordResetForm

email_label = "Enter your email address below, and we'll email instructions for setting a new one."


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=email_label, max_length=254)
