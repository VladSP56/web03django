from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField('Название', max_length=255)
    short_description = models.TextField('Краткое описание')
    full_description = models.TextField('Полное описание новости')
    publication_date = models.DateField('Дата публикации')
    publication_time = models.TimeField('Время публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
