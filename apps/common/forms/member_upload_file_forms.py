from django import forms

from common.models.member_model import Member


class MemberUploadFileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('image', 'image_title')

    def __init__(self, *args, **kwargs):
        super(MemberUploadFileForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        # member = Member.objects.get(id_member=self.fields['id_member'])
        # member.image = self.fields['id_member']
        # member.image_title = self.fields['image_title']