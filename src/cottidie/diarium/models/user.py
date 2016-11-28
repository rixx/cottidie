from django.conf import settings
from django.db import models


class DiariumProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='diarium')
    default = models.OneToOneField('Notebook')
