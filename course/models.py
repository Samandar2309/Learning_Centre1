from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Teacher(TimeStampedModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    experience = models.CharField(max_length=212)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Course(TimeStampedModel):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    teachers = models.CharField(max_length=600, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    term = models.CharField(max_length=40)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
