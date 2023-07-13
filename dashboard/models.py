from django.db import models

# Create your models here.

class Invoice(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    package = models.CharField(max_length=100)
    package_rate = models.IntegerField()
    arrival_date = models.DateField()
    departure_date = models.DateField()
    today_date = models.DateField()
    prepayment = models.DecimalField(max_digits=30, decimal_places=2)
    total = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.name
