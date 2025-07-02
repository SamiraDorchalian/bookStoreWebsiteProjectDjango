from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomeUserCreationForm, CustomeUserChangeForm
from .models import CustomeUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    model = CustomeUser
    list_display = ['username', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )


admin.site.register(CustomeUser, CustomUserAdmin)
