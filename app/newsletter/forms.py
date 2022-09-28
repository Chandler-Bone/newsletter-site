from django.forms import ModelForm
from newsletter.models import RegisteredUser
from django import forms

class RegisteredUserForm(ModelForm):
    #use helper class to make the form using registereduser model
    class Meta:
        model = RegisteredUser
        fields = '__all__'

    #built-in hook method to make all names be capitalized on entry
    def clean_name(self):
        return self.cleaned_data['name'].title()
