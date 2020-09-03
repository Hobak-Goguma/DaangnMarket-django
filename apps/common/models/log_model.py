from datetime import datetime

from django.db import models

from common.models.member_model import Member


class Log(models.Model):
	id_log: int = models.AutoField(primary_key=True)
	id_member: Member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_member')
	search: str = models.CharField(max_length=60)
	cdate: datetime = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'log'
