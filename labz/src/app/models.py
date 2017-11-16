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


class Student(models.Model):
    name = models.TextField(max_length=120)
    surname = models.TextField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    bio = models.TextField()
    #group = models.OneToOneField(Group, on_delete=models.CASCADE)
    def __unicode__(self):
        return u"%s %s %s "%(self.name, self.surname,self.bio)

    def __str__(self):
           return u"%s %s %s "%(self.name, self.surname,self.bio)

class Teacher(models.Model):

    name = models.TextField(max_length=120)
    surname = models.TextField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="150px",
            height_field="150px")
    bio = models.TextField()
    courser = models.OneToOneField(Course, on_delete=models.CASCADE)
    def __unicode__(self):
        return u"%s %s %s %s"%(self.name, self.surname,self.bio,self.courser)

    def __str__(self):
           return u"%s %s %s %s"%(self.name, self.surname,self.bio,self.courser)


class Group(models.Model):
    title=models.TextField(max_length=20)
    course = models.TextField(max_length=15)
    the_elder = models.TextField(max_length=12)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s %s %s %s"%(self.the_elder, self.title,self.course,self.students)

    def __str__(self):
           return u"%s %s %s %s"%(self.the_elder, self.title,self.course,self.students)

class Course(models.Model):
    info = models.TextField(max_length=123)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s %s "%(self.teacher, self.info,)

    def __str__(self):
        return u"%s %s "%(self.teacher, self.info,)
