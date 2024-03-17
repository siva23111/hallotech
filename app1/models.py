from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# projects/models.py

def validate_min_words(value):
    min_words = 200
    words = value.split()
    if len(words) < min_words:
        raise ValidationError(f'The description must have a minimum of {min_words} words.')


class Post(models.Model):
    PROJECT_CHOICES = [
        ('AI/ML', 'AI/ML'),
        ('Web Development', 'Web Development'),
        ('IoT Projects', 'IoT Projects'),
        ('Hardware Projects', 'Hardware Projects'),
        ('Media Creations', 'Media Creations'),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    description = models.TextField(validators=[validate_min_words])

    def __str__(self):
        return self.title
