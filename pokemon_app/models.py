from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    image_url = models.URLField()
    
    def __str__(self):
        return self.name