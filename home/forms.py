from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'type': "text",
        'placeholder': "Name",
    }), label='name')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'type': "email",
        'placeholder': "Email",
    }), label='email')
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'placeholder': "Type your message",
    }), label='message')
    class Meta:
        model = Contact
        fields = '__all__'
