from django.db import models


class MannerReviewer(models.Model):
    id_manner_log = models.ForeignKey('common.MannerLog', models.DO_NOTHING, db_column='id_manner_log')
    reviewer = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='reviewer')

    class Meta:
        db_table = 'manner_reviewer'
        app_label = 'common'