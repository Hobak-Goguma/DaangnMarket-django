from django.db import models

class Rate(models.Model):
    id_rate = models.IntegerField(primary_key=True)
    field = models.CharField(max_length=8)
    detail = models.CharField(max_length=50)
    score = models.FloatField()

    class Meta:
        db_table = 'rate'
        app_label = 'common'
