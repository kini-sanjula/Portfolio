from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description= models.CharField(max_length=300)
    image=models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
