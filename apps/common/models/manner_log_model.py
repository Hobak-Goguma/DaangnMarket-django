from django.db import models


class MannerLog(models.Model):
    id_manner_log = models.IntegerField(primary_key=True)
    id_manner = models.ForeignKey('common.Manner', models.DO_NOTHING, db_column='id_manner')
    score = models.FloatField()
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'manner_log'
        app_label = 'common'