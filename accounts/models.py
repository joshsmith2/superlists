from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class ListUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'joshsmith2@gmail.com'

    @property
    def is_active(self):
        return True
