from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models


class Visit(models.Model):
    session_key = models.CharField(max_length=255)
    ip_address = models.IPAddressField(blank=True)
    referer = models.URLField(blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=5)
    timestamp = models.DateTimeField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = datetime.now()
        super(Visit, self).save(*args, **kwargs)


class IPFilter(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.IPAddressField()
    account = models.ForeignKey(User, blank=True, null=True)
