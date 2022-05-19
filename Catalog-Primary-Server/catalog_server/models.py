from django.db import models

# Create your models here.


class Book(models.Model):
    number_of_items = models.IntegerField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=80, null=True)
    title = models.CharField(max_length=50, null=True)


    def __str__(self):
        return f"{self.title}"

