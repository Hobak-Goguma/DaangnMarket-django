from django.db import models


class Rate(models.Model):
	id_rate: int = models.IntegerField(primary_key=True)
	field: str = models.CharField(max_length=8)
	detail: str = models.CharField(max_length=50)
	score: int = models.FloatField()

	class Meta:
		db_table = 'rate'
		app_label = 'common'
