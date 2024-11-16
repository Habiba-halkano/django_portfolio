from django import forms
from django.core.exceptions import ValidationError

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message',
                'rows': 3,
            }),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 100:
            raise forms.ValidationError("The message must be at least 100 characters long.")
        return message

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 10:
            raise ValidationError('Please enter a valid 10-digit phone number.')
        return phone