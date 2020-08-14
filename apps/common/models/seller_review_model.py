from django.db import models


class SellerReview(models.Model):
    id_review_seller = models.AutoField(primary_key=True)
    id_seller = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_seller')
    content = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'seller_review'
        app_label = 'common'