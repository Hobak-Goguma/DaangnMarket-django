from datetime import datetime

from django.db import models

from common.models.member_model import Member


class Manner(models.Model):
	id_manner: int = models.AutoField(primary_key=True)
	id_member: Member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_member')
	score: int = models.FloatField()
	cdate: datetime = models.DateTimeField(auto_now_add=True)
	udate: datetime = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'manner'
