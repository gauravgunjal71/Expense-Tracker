from django.db import models

# Create your models here.
class Expense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name