from datetime import datetime

from django.db import models

from common.models.member_model import Member
from posts.models.product_model import Product


class Wishlist(models.Model):
    id_wishlist: int = models.AutoField(primary_key=True)
    id_product: Product = models.ForeignKey('posts.Product', models.PROTECT, db_column='id_product')
    id_member: Member = models.ForeignKey('common.Member', models.PROTECT, db_column='id_member')
    cdate: datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wishlist'