from django import forms

from .models import Topic, Entry, Comment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text", "public"]
        labels = {
            "text": "",
            "public": "Public - available to be viewed by all users. Only you can modify it and add new entries",
        }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        # widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        # widgets = {
        #     "comment": forms.Textarea(attrs={"rows": 3, "cols": 40}),
        # }
