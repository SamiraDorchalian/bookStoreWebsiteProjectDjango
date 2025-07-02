from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomeUser


class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = UserCreationForm.Meta.fields + ('age', )


class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomeUser
        fields = UserChangeForm.Meta.fields