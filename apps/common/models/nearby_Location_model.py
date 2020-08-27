from django.db import models


class NearbyLocation(models.Model):
	id_nearby_location = models.AutoField(primary_key=True)
	dong = models.ForeignKey('common.Location', models.DO_NOTHING, db_column='dong')
	nearby_dong = models.CharField(max_length=20)
	distance = models.IntegerField()

	class Meta:
		db_table = 'nearby_location'
		unique_together = (('dong', 'nearby_dong', 'distance'),)
