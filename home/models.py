from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Fact(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    image = models.ImageField(upload_to='images/icon-image/')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(default='Morbi turpis nisl, auctor ut nisl vel, pellentesque euismod nunc nunc accumsan imperdiet.')
    location = models.CharField(max_length=100, default='McLean, VA')
    client = models.CharField(max_length=100, default='Pransbay Powers Authority')
    architect = models.CharField(max_length=100, default='Dlarke Pelli Incorp')
    size = models.IntegerField()
    image = models.ImageField(upload_to='images/projects/')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name