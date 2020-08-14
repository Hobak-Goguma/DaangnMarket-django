from django.db import models


class Manner(models.Model):
    id_manner = models.AutoField(primary_key=True)
    id_member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_member')
    score = models.FloatField()
    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'manner'
        app_label = 'common'