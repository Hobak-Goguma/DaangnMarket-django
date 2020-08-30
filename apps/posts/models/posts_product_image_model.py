import os

from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField

# from member.serializers import ProductImageSerializer
from posts.models.product_model import Product


class ProductImage(models.Model):
    def __str__(self):
        return self.image.url
    id_product: Product = models.ForeignKey('posts.Product', on_delete=models.CASCADE, db_column='id_product', related_name='thum')
    id_product_img: int = models.AutoField(primary_key=True)
    image_title: str = models.CharField(default='', max_length=50)
    image: ProcessedImageField = ProcessedImageField(
        null=True, 
        upload_to="product",
        format = 'JPEG',
        )
    
    # @property
    # def thum_first(self):
    #     return self.image.filter()

# TODO 확장자 화이트 리스트 함수 작성
    # def image_tag(self):
    #     return u'<img src="%s" width="300"/>' % self.image.url #Not bad code
    # image_tag.allow_tags = True

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(ProductImage, self).delete(*args, **kargs)

    class Meta:
        db_table = 'posts_product_image'
        app_label = 'posts'