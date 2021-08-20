from django import forms

class event_contact(forms.Form):
    name=forms.CharField(label="Name",max_length=10)
    info=forms.CharField(label="Contact Information",max_length=100)
    text=forms.CharField(label="Proposition",max_length=1000)
   