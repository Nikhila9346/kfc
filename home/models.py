from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Menu(models.Model):
    item = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(default='/no_image.png',upload_to='items/')

    def __str__(self):
        return self.item
    
class Cart(models.Model):
    item = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    
    def __str__(self):
        return self.item