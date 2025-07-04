from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomeUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Age'))