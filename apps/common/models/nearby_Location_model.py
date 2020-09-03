from django.db import models

from common.models.location_model import Location


class NearbyLocation(models.Model):
	id_nearby_location: int = models.AutoField(primary_key=True)
	dong: Location = models.ForeignKey('common.Location', models.DO_NOTHING, db_column='dong')
	nearby_dong: str = models.CharField(max_length=20)
	distance: int = models.IntegerField()

	class Meta:
		db_table = 'nearby_location'
		unique_together = (('dong', 'nearby_dong', 'distance'),)
