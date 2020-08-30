from django import forms

from posts.models.posts_product_image_model import ProductImage


class ProductUploadFileForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image_title', 'image', 'id_product')

    def __init__(self, *args, **kwargs):
        super(ProductUploadFileForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False