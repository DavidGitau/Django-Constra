from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
    
class Category(CommonInfo):
    class Meta:
        verbose_name_plural = 'Categories'


class Fact(CommonInfo):
    number = models.IntegerField()
    image = models.ImageField(upload_to='images/icon-image/')

class Project(CommonInfo):
    about = models.TextField(default='Morbi turpis nisl, auctor ut nisl vel, pellentesque euismod nunc nunc accumsan imperdiet.')
    location = models.CharField(max_length=100, default='McLean, VA')
    client = models.CharField(max_length=100, default='Pransbay Powers Authority')
    architect = models.CharField(max_length=100, default='Dlarke Pelli Incorp')
    size = models.IntegerField()
    image = models.ImageField(upload_to='images/projects/')
    categories = models.ManyToManyField(Category)

class Team(CommonInfo):
    about = models.TextField(default='Morbi turpis nisl, auctor ut nisl vel, pellentesque euismod nunc nunc accumsan imperdiet.')
    position = models.CharField(max_length=100, default='Dlarke Pelli Incorp')
    image = models.ImageField(upload_to='images/team/')
