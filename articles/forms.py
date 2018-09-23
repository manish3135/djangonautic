from django import forms
from .models import Article


class CreateArticle(forms.ModelForm):
    class Meta():
        model = Article
        fields = ('title','body','slug','thumb')
        widgets = {
        'title' : forms.TextInput(attrs={'class':'input','autofocus':True}),
        'slug' : forms.TextInput(attrs={'class':'input','autofocus':True}),

        }
