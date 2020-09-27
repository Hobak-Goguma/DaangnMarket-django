from django.db import models

from common.models.manner_log_model import MannerLog
from common.models.member_model import Member


class MannerReviewer(models.Model):
	id_manner_log: MannerLog = models.ForeignKey('common.MannerLog', models.DO_NOTHING, db_column='id_manner_log')
	reviewer: Member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='reviewer')

	class Meta:
		db_table = 'manner_reviewer'
