from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    PROJECT_CHOICES = [
        ('residential', 'Turar-joy interyeri'),
        ('commercial', 'Tijorat interyeri'),
        ('architecture', 'Arxitektura'),
        ('other', 'Boshqa'),
    ]
    project_type = forms.ChoiceField(choices=PROJECT_CHOICES, required=False)

    class Meta:
        model = ContactMessage
        fields = ['project_type', 'area', 'address', 'name', 'phone']
        widgets = {
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите площадь (кв.м)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите адрес объекта'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш номер телефона'}),
        }
