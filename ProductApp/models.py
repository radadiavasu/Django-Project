from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=20)
    catImage = models.ImageField(upload_to="category")

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    category = models.ManyToManyField(CategoryModel)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.name