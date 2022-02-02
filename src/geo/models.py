from django.contrib.gis.db import models

# Create your models here.

class Trader(models.Model):
    trading_name = models.CharField(max_length=256)
    owner_name = models.CharField(max_length=256)
    document = models.CharField(max_length=128, unique=True, db_index=True)
    address = models.PointField()
    coverage_area = models.MultiPolygonField()
