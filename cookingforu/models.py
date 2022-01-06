from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255 ,null=False ,blank=False)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    video = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name