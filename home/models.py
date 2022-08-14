from django.db import models

class Fact(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    image = models.ImageField(upload_to='images/icon-image/')

    def __str__(self):
        return self.name