from django.db import models

class Saver(models.Model):
    code = models.CharField(
    max_length=20,
    unique=True,
    editable=False,
    null=True,
    blank=True
)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=13, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)  # ✅ แก้ตรงนี้
    phone = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.code:
            last = Saver.objects.order_by('-id').first()
            if last:
                last_code = int(last.code.replace('SG', ''))
                new_code = last_code + 1
            else:
                new_code = 1

            self.code = f"SG{new_code:04d}"  # SG0001
        super().save(*args, **kwargs)
    
class GoldSaving(models.Model):
    saver = models.ForeignKey(Saver, on_delete=models.CASCADE, null=True, blank=True)  # ✅ แก้ตรงนี้
    gold_weight = models.FloatField()
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.saver.first_name} {self.saver.last_name} - {self.gold_weight}g"

