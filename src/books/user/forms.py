from user.models import User

from django import forms


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'age')
