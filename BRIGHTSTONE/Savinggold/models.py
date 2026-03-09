from django.db import models

# Create your models here.
from django.db import models

class Saver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class GoldSaving(models.Model):
    saver = models.ForeignKey(Saver, on_delete=models.CASCADE)
    gold_weight = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.saver.first_name} {self.saver.last_name} - {self.gold_weight}g"

