from django.db import models


class NearbyLocation(models.Model):
    dong = models.OneToOneField('common.Location', models.DO_NOTHING, db_column='dong', primary_key=True, unique=True)
    nearby_dong = models.CharField(max_length=20)
    distance = models.IntegerField()

    class Meta:
        db_table = 'nearby_location'
        app_label = 'common'
        unique_together = (('dong', 'nearby_dong', 'distance'),)