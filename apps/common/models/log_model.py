from django.db import models


class Log(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_member')
    search = models.CharField(max_length=60)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'log'
        app_label = 'common'