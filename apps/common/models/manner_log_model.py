from datetime import datetime

from django.db import models

from common.models.manner_model import Manner


class MannerLog(models.Model):
	id_manner_log: int = models.IntegerField(primary_key=True)
	id_manner: Manner = models.ForeignKey('common.Manner', models.DO_NOTHING, db_column='id_manner')
	score: int = models.FloatField()
	cdate: datetime = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'manner_log'
