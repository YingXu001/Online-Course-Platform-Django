from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    description = models.TextField(verbose_name='description')
    teacher = models.CharField(max_length=50, null=True, blank=True, verbose_name='teacher')
    click = models.IntegerField(default=0, verbose_name='click')
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium',
                                  verbose_name='difficulty')
    comment = models.TextField(verbose_name='comment', default='No comment provided')
    # comment = models.TextField(verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create_time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update_time')

    def __str__(self):
        return self.title


