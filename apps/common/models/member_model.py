import os
from django.conf import settings
from datetime import datetime

from django.db import models
from imagekit.models import ProcessedImageField


class Member(models.Model):

	def upload_to_id_image(instance, filename):
		extension = os.path.splitext(filename)[1].lower()
		path = 'member/%(id)s_%(date_now)s' % {
			'id': instance.user_id,
			'date_now': datetime.now().date().strftime("%Y%m%d")}
		return '%(path)s%(extension)s' % {'path': path,
		                                  'extension': extension}

	id_member: int = models.AutoField(primary_key=True)
	name: str = models.CharField(max_length=30)
	user_id: str = models.CharField(unique=True, max_length=30)
	user_pw: str = models.CharField(max_length=300)
	nick_name: str = models.CharField(max_length=30)
	tel: str = models.CharField(max_length=20)
	birth = models.DateField(null=True, blank=True)
	email: str = models.CharField(max_length=30, blank=True)
	gender: str = models.CharField(max_length=6, blank=True)
	cdate: datetime = models.DateTimeField(auto_now_add=True)
	udate: datetime = models.DateTimeField(auto_now=True, null=True, blank=True)
	last_date: datetime = models.DateTimeField(auto_now=False, null=True, blank=True)
	image_title: str = models.CharField(default='', max_length=50)
	image: ProcessedImageField = ProcessedImageField(
		null=True,
		upload_to=upload_to_id_image,
		format='JPEG',
	)

	class Meta:
		db_table = 'member'

	def delete_image(self, *args, **kargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
		self.image = None
		self.image_title = ''
		self.save()
