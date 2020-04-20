from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forms.models import *
from django import forms
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    # Initate the css class for all fields 
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self: 
            field.field.widget.attrs['class'] =  'form-control'

class FormCreationForm(forms.ModelForm):
    class Meta:
        model = Form
        #fields = '__all__'
        fields = ('title', 'intro', 'button_text', 'response', 'publish_date','expiry_date')

    # Initate the css class for all fields 
    def __init__(self, *args, **kwargs):
        super(FormCreationForm, self).__init__(*args, **kwargs)
        for field in self: 
            field.field.widget.attrs['class'] =  'form-control'

class FieldCreationForm(forms.ModelForm):
    class Meta:
        model = Field
        #fields = '__all__'
        fields = ('label', 'field_type', 'required', 'choices', 'placeholder_text','help_text')
     # Initate the css class for all fields 
    def __init__(self, *args, **kwargs):
        super(FieldCreationForm, self).__init__(*args, **kwargs)
        for field in self: 
            field.field.widget.attrs['class'] =  'form-control'
  
FormCreationSet = inlineformset_factory(Form, Field, form = FieldCreationForm, extra=3)