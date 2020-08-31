from django import forms

from posts.models.company_image_model import CompanyImage


class CompanyUploadFileForm(forms.ModelForm):
    class Meta:
        model = CompanyImage
        fields = ('image_title', 'image', 'id_company')

    def __init__(self, *args, **kwargs):
        super(CompanyUploadFileForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False