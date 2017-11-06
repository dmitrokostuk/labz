from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
# Create your tests here.
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)


class Profesor(models.Model):
    name = models.TextField(max_length=120)
    midlename = models.TextField(max_length=120)
    surname = models.TextField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    bio = models.TextField()
    courser = models.TextField(max_length=120)