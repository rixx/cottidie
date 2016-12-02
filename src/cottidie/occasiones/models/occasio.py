from django.conf import settings
from django.db import models
from django.utils.timezone import now


class OccasionType(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='occasion_types')
    name = models.CharField(null=True, blank=True, max_length=250)

    def __str__(self):
        return 'Occasion type "{self.name}" of user {self.user}'.format(self=self)


class Occasion(models.Model):
    typus = models.ForeignKey('OccasionType', related_name='occasiones')
    note = models.CharField(null=True, blank=True, max_length=1500)
    start = models.DateTimeField(default=now)
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{typus} occasion on {date} ({user})'.format(
            typus=self.typus,
            date=self.start.strftime('%Y-%m-%d'),
            user=self.typus.user,
        )
