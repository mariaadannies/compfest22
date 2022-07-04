from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    image = ImageField(blank=False, null=False)

    desc = models.CharField(default="", max_length=200, blank=False)

    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, blank=False)

    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    