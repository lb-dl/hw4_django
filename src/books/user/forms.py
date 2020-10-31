from user.models import User

from django import forms


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'age')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = user.first_name.title()
        user.last_name = user.last_name.title()
        user.save()
        return user
