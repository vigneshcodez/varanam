from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Location(models.Model):
    image = models.ImageField(upload_to='location/')
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name=models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    company = models.CharField(max_length=25)
    description=models.TextField()
    image=models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.name