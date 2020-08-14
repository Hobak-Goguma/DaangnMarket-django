from django.db import models


class ShopperRate(models.Model):
    id_review_shopper = models.ForeignKey('common.ShopperReview', models.DO_NOTHING, db_column='id_review_shopper')
    id_rate = models.ForeignKey('common.Rate', models.DO_NOTHING, db_column='id_rate')

    class Meta:
        db_table = 'shopper_rate'
        app_label = 'common'