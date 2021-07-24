from django import forms
from tags.models import Tag


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'})
    }
