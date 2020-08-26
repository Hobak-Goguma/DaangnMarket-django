from datetime import datetime

from django.db import models

from common.models.member_model import Member


class Company(models.Model):
    id_company: int = models.AutoField(primary_key=True)
    id_member: Member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_member')
    name: str = models.CharField(max_length=50)
    addr: str = models.CharField(max_length=200)
    tel: str = models.CharField(max_length=20, blank=True, null=True)
    info: str = models.CharField(max_length=3000, blank=True, null=True)
    category = models.CharField(max_length=15, blank=True, null=True)
    img: str = models.CharField(max_length=2000, blank=True, null=True)
    cdate: datetime = models.DateTimeField(auto_now_add=True)
    udate: datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'company'
        app_label = 'posts'