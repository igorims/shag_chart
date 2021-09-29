from django.forms import ModelForm
from django import forms

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'date_posted', 'time_posted')

        widgets = {
            'date_posted': forms.SelectDateWidget(),
            'time_posted': forms.TimeInput(attrs={
                'value': '12:00:00'
            }),
        }