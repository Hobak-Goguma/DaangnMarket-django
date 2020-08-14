from django.db import models


class Wishlist(models.Model):
    id_wishlist = models.AutoField(primary_key=True)
    id_product = models.ForeignKey('common.Product', models.PROTECT, db_column='id_product')
    id_member = models.ForeignKey('common.Member', models.PROTECT, db_column='id_member')
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wishlist'
        app_label = 'common'