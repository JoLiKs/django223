from django.db import models
from django.db.models import CharField


class Users(models.Model):
    login = CharField(max_length=10)
    password = CharField(max_length=10)