from django import forms

class ContactForm(forms.Form):
    message_area = forms.CharField(label="",widget=forms.Textarea)
