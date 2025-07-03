from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomeUser


class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = ('username', 'age', 'email', )


class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomeUser
        fields = ('username', 'age', 'email', )