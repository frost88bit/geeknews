from django import forms

from .models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields =(
            'pic',
            'link',
            'title',
            'date'
        )
        widgets = {
            'pic' : forms.URLInput,
            'link' : forms.URLInput,
            'title' : forms.TextInput, 
        }