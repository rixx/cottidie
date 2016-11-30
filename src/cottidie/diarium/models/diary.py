from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Notebook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='diaria')
    title = models.CharField(null=True, blank=True, max_length=250)
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.modified = now()

        if 'update_fields' in kwargs:
            kwargs['update_fields'] += ['modified']

        super().save(*args, **kwargs)

    def __str__(self):
        if self.title:
            return 'Notebook {self.title} by {self.user}'.format(self=self)
        return 'Notebook #{self.pk} by {self.user}'.format(self=self)


class Entry(models.Model):
    notebook = models.ForeignKey('Notebook', related_name='entries')
    text = models.TextField(null=True, blank=True)
    word_count = models.PositiveIntegerField(default=0)
    character_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.modified = now()

        if 'update_fields' in kwargs:
            kwargs['update_fields'] += ['modified']

        super().save(*args, **kwargs)

    def __str__(self):
        return 'Entry on {date} in {notebook}'.format(
            date=self.created.strftime('%Y-%m-%d'),
            notebook=str(self.notebook),
        )
