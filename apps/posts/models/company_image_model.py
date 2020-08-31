import os
from datetime import datetime

from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField

from posts.models.company_model import Company


class CompanyImage(models.Model):

	def upload_to_id_image(instance, filename):
		name: str = Company.objects.get(id_company=instance.id_company).name
		extension = os.path.splitext(filename)[1].lower()
		if extension != '.jpg' or '.jpeg':
			extension = '.jpg'
		path = 'company/%(id)s_%(date_now)s' % {
			'id': name,
			'date_now': datetime.now().date().strftime("%Y%m%d")}
		return '%(path)s%(extension)s' % {'path': path,
		                                  'extension': extension}

	id_company: Company = models.ForeignKey('posts.Company', on_delete=models.CASCADE, db_column='id_company',
	                                        related_name='thum')
	image_title: str = models.CharField(default='', max_length=50)
	image: ProcessedImageField = ProcessedImageField(
		null=True,
		upload_to=upload_to_id_image,
		format='JPEG',
	)

	class Meta:
		db_table = 'company_image'

	def delete(self, *args, **kargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
		super(CompanyImage, self).delete(*args, **kargs)
