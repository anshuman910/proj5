from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='Covers/', blank=True)
    pages = models.IntegerField(max_length=7, default=0, blank=True)
