from typing_extensions import override
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Data
from django.db import models

data = Data.objects.all()


PARENT_CONSTITUENCY_CHOICES = [('karanja@karanja.com', 'Karanja'), ('ashti@ashti.com', 'Ashti'), ('arvi@arvi.com', 'arvi')]




class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':'Full Name'}))
    choices = [(0,'User'), (1,'Admin'), (2, 'Superuser')]
    last_name = forms.ChoiceField(label='Status', choices=choices, widget=forms.Select(attrs={'class':"form-control", 'placeholder':'Status'}))
    email = forms.ChoiceField(label='Status', choices=PARENT_CONSTITUENCY_CHOICES, widget=forms.Select(attrs={'class':"form-control", 'placeholder':'Parent Constituency'}))
     
    
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        

    def  __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

        

    
        


class AddDataForm(forms.ModelForm):
    
    polling_booth_number    =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'polling_booth_number', 'class': 'form-control'}), label='')
    polling_booth_name      =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'polling_booth_name', 'class': 'form-control'}), label='')
    parent_constituency     =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'parent_constituency', 'class': 'form-control'}), label='')
    winner2014              =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'winner2014', 'class': 'form-control'}), label='')
    runner_up               =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'runner_up', 'class': 'form-control'}), label='')
    margin1_percent         =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'margin1_percent', 'class': 'form-control'}), label='')
    margin1                 =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'margin1', 'class': 'form-control'}), label='')
    total_voters            =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'total_voters', 'class': 'form-control'}), label='')
    bjp1_votes              =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'bjp1_votes', 'class': 'form-control'}), label='')
    bjp1_vote_percent       =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'bjp1_vote_percent', 'class': 'form-control'}), label='')
    inc1_votes              =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'inc1_votes', 'class': 'form-control'}), label='')
    inc1_votes_percent      =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'inc1_votes_percent', 'class': 'form-control'}), label='')
    winner2019              =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'winner2019', 'class': 'form-control'}), label='')
    margin2_percent         =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'margin2_percent', 'class': 'form-control'}), label='')
    margin2                 =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'margin2', 'class': 'form-control'}), label='')
    total2_voters           =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'total2_voters', 'class': 'form-control'}), label='')
    bjp2_votes              =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'bjp2_votes', 'class': 'form-control'}), label='')
    bjp2_votes_percent      =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'bjp2_votes_percent', 'class': 'form-control'}), label='')
    inc2_votes              =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'inc2_votes', 'class': 'form-control'}), label='')
    inc2_vote_percent       =   forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'placeholder':'inc2_vote_percent', 'class': 'form-control'}), label='')
    

    class Meta:
        model=Data
        exclude=("user",)

