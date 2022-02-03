from django.db import models


class Profile(models.Model):
    USER_ROLES = [("User", 'User'), ("Admin", 'Admin')]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=USER_ROLES, default="User")

    def __str__(self):
        return self.name
