from django import forms
from .models import Website, StatusPage

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'url', 'check_interval']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My Website'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'check_interval': forms.Select(
                choices=[
                    (60, '1 minute'),
                    (300, '5 minutes'),
                    (600, '10 minutes'),
                    (1800, '30 minutes'),
                ],
                attrs={'class': 'form-control'}
            ),
        }

class StatusPageForm(forms.ModelForm):
    class Meta:
        model = StatusPage
        fields = ['slug', 'title', 'description', 'is_public']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'my-company'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My Company Status'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }