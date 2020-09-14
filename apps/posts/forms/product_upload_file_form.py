from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from posts.models.posts_product_image_model import ProductImage


class ProductUploadFileForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image_title', 'image', 'id_product')

    def clean_image(self):
        data = self.cleaned_data['image']
        image_count = ProductImage.objects.filter(id_product=self.data['id_product']).count()
        if image_count >= 10:
            raise ValidationError(_("Allow up to 10 images."), code='invalid')
        return data

    def __init__(self, *args, **kwargs):
        super(ProductUploadFileForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False