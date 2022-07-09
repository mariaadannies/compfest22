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

class Balance(models.Model):
    starting_balance = 100000.00

    add_balance = models.DecimalField(default=0.00, blank=False, max_digits=30, decimal_places=2)

    withdraw_balance = models.DecimalField(default=0.00, blank=False, max_digits=10, decimal_places=2)

    def get_balance(self):
        return self.starting_balance

    def withdraw_balance(self, withdraw_amount):

        if withdraw_amount < self.starting_balance:
            self.starting_balance - withdraw_amount
        else:
            self.starting_balance = 0.00

        return self.get_balance

    def add_balance(self, add_amount):
        self.starting_balance - add_amount

        return self.get_balance

    