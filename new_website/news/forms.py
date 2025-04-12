from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'short_description', 'full_description', 'publication_date', 'publication_time']