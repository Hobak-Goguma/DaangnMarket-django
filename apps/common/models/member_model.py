import os
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField


class Member(models.Model):
	def upload_to_id_image(instance, filename):
		extension = os.path.splitext(filename)[1].lower()
		if extension != '.jpg' or '.jpeg':
			extension = '.jpg'
		path = 'member/%(id)s_%(date_now)s' % {
			'id': instance.user_id,
			'date_now': datetime.now().strftime("%Y%m%d%H%M%S")}
		return '%(path)s%(extension)s' % {'path': path,
		                                  'extension': extension}

	id_member: int = models.AutoField(primary_key=True)
	name: str = models.CharField(max_length=30)
	user_id: str = models.CharField(unique=True, max_length=30)
	user_pw: str = models.CharField(max_length=300)
	nick_name: str = models.CharField(max_length=30)
	tel: str = models.CharField(max_length=20)
	birth: datetime = models.DateField(null=True, blank=True)
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
	auth: int = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='auth', related_name='auth', default=None, blank=True, null=True)

	# objects = MemberManager()

	class Meta:
		db_table = 'member'

	def delete_image(self, *args, **kargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
		self.image = None
		self.image_title = ''
		self.save()

	def save(self, *args, **kwargs):
		if not self.pk:
			user = User.objects.create_user(username=self.user_id, email=self.email)
			user.set_password(self.user_pw)
			self.auth = user
			self.user_pw = user.password
		super(Member, self).save(*args, **kwargs)
