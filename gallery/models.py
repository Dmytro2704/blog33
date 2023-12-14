from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='uploads', default='default_image.jpg')
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

