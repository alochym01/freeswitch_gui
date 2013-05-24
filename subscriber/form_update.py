from django import forms
from models import fsUser


class fsUserFormUpdate(forms.ModelForm):
    class Meta:
        model = fsUser
        fields = ('id', 'Username', 'Password', 'Toll_allow', 'User_context')
