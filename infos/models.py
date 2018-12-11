from django.db import models

# Create your models here.


class tbValues(models.Model):

    barcode_num = models.CharField(max_length=30)
    freeze_num = models.CharField(max_length=10)
    box_num = models.CharField(max_length=10)
    rack_num = models.CharField(max_length=10)
    well_num = models.CharField(max_length=10)

    def __str__(self):
        return self.barcode_num
