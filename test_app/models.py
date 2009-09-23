from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class Widget(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Widget, self).save(*args, **kwargs)
