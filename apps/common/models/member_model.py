import os
from django.conf import settings
from datetime import datetime

from django.db import models
from imagekit.models import ProcessedImageField



class Member(models.Model):
    id_member: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=30)
    user_id: str = models.CharField(unique=True, max_length=30)
    user_pw: str = models.CharField(max_length=300)
    nick_name: str = models.CharField(max_length=30)
    tel: str = models.CharField(max_length=20)
    birth = models.DateField(null=True)
    email: str = models.CharField(max_length=30)
    gender: str = models.CharField(max_length=6)
    cdate: datetime = models.DateTimeField(auto_now_add=True)
    udate: datetime = models.DateTimeField(auto_now=False, null=True)
    last_date: datetime = models.DateTimeField(auto_now=False, null=True)
    image: ProcessedImageField = ProcessedImageField(
        null=True,
        upload_to="User",
        format='JPEG',
    )

    class Meta:
        db_table = 'member'
        app_label = 'common'

    def delete_image(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.path))
        super().delete(*args, **kargs)