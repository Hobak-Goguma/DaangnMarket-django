from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from posts.models.company_image_model import CompanyImage


class CompanyUploadFileForm(forms.ModelForm):
    class Meta:
        model = CompanyImage
        fields = ('image_title', 'image', 'id_company')

    def clean_image(self):
        data = self.cleaned_data['image']
        image_count = CompanyImage.objects.filter(id_company=self.data['id_company']).count()
        if image_count >= 10:
            raise ValidationError(_("Allow up to 10 images."), code='invalid')
        return data

    def __init__(self, *args, **kwargs):
        super(CompanyUploadFileForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False