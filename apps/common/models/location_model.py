from django.db import models

class Location(models.Model):
    dong: str = models.CharField(primary_key=True, max_length=20)
    latitude: int = models.DecimalField(max_digits=11, decimal_places=8)
    longitude: int = models.DecimalField(max_digits=11, decimal_places=8)
    gu: str = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'location'