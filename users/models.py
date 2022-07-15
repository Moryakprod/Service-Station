from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("MASTER", "Master"),
    )

    _role = models.CharField(_("role"), max_length=6, choices=ROLE_CHOICES, default='')

    @property
    def user_role(self):
        return self._role
