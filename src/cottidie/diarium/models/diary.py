from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Notebook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(null=True, blank=True, max_length=250)
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        kwargs['modified'] = now()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.title:
            return 'Notebook {self.title} by {self.user}'.format(self=self)
        return 'Notebook #{self.pk} by {self.user}'.format(self=self)


class Entry(models.Model):
    notebook = models.ForeignKey('Notebook')
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        kwargs['modified'] = now()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Entry on {date} in {notebook}'.format(
            date=self.created.strftime('%Y-%m-%d'),
            notebook=str(self.notebook),
        )
