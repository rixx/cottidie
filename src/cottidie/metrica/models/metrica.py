from django.conf import settings
from django.db import models

TYPES = [
    'NUMS', 'MULTIVAL', 'TEXT',  # Generic types
    'WEIGHT',  # More specific subtypes for better texting/graphs
]


class Metric(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='metrics')
    name = models.CharField(null=True, blank=True, max_length=250)
    type_choice = models.CharField(max_length=10, choices=((t, t) for t in TYPES))

    def __str__(self) -> str:
        return 'Metric {self.name} of type {self.type}'.format(self=self)


class Goal(models.Model):
    metric = models.ForeignKey('Metric', related_name='goals')
    text = models.CharField(max_length=1000)
    motivation_text = models.CharField(max_length=10000, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return 'Goal of "{goal}" for metric {metric}'.format(
            goal = self.text if len(self.text) < 10 else self.text[:9] + '…',
            metric = self.metric.name,
        )


class Measurement(models.Model):
    metric = models.ForeignKey('Metric', related_name='measurements')
    value = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now=True)
