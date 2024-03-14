from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Categ(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to='cat_icon')

    def get_url(self):
        return reverse('prod_cat', args=[self.slug])


class Products(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to='product')
    des = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField()
    category = models.ForeignKey(Categ, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details', args=[self.category.slug, self.slug])


