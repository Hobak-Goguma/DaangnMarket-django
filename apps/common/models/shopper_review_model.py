from django.db import models


class ShopperReview(models.Model):
    id_review_shopper = models.AutoField(primary_key=True)
    id_real_deal = models.ForeignKey('common.RealDeal', models.DO_NOTHING, db_column='id_real_deal')
    content = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shopper_review'
        app_label = 'common'
