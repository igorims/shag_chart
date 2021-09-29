from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField('Заголовок',max_length=30)
    content = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField('Дата поста')
    time_posted = models.TimeField('Время поста', null=True, blank=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
