from django import forms
from models import fsUser


class fsUserForm(forms.ModelForm):
    class Meta:
        model = fsUser
        fields = ('Username', 'Password', 'Toll_allow', 'User_context')
