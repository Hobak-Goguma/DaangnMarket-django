from django.db import models


class Memberaddr(models.Model):
	id_member_addr: int = models.AutoField(primary_key=True)
	id_member: int = models.ForeignKey('Member', models.DO_NOTHING, db_column='id_member')
	addr: str = models.CharField(max_length=200)
	distance: int = models.IntegerField(default=0)
	select: str = models.CharField(max_length=8, default="Y")

	class Meta:
		db_table = 'member_addr'
		app_label = 'common'
