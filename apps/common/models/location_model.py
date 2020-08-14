from django.db import models

class Location(models.Model):
    dong = models.CharField(primary_key=True, max_length=20)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    gu = models.CharField(max_length=30)

    class Meta:
        db_table = 'location'
        app_label = 'common'