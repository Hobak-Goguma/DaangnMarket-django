from django.db import models


class Memberaddr(models.Model):
    id_member_addr = models.AutoField(primary_key=True)
    id_member = models.ForeignKey('Member', models.DO_NOTHING, db_column='id_member')
    addr = models.CharField(max_length=200)
    distance = models.IntegerField(default=0)
    select = models.CharField(max_length=8, default="Y")

    class Meta:
        db_table = 'member_addr'
        app_label = 'common'