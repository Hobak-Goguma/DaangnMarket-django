from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from common.models.member_addr_model import Memberaddr
from common.models.location_model import Location


class MemberAddrForm(forms.ModelForm):
    class Meta:
        model = Memberaddr
        fields = ('id_member', 'addr', 'distance')

    def clean_addr(self):
        addr = self.cleaned_data['addr']
        try:
            address = Location.objects.get(dong=addr)
        except Location.DoesNotExist:
            raise ValidationError(_("Address does not exist"), code='invalid')
        return addr

    def clean_distance(self):
        dis = self.cleaned_data['distance']
        allow_distance = [0, 2, 5, 10, 15]
        if dis not in allow_distance:
            raise ValidationError(_("Allow distance is " + str(allow_distance)), code='invalid')
        return dis

    def user_addr(self):
        id_member = self.data['id_member']
        addr = self.data['addr']
        try:
            member = Memberaddr.objects.filter(id_member=id_member).get(addr=addr)
        except Memberaddr.DoesNotExist:
            return False
        return True

    def __init__(self, *args, **kwargs):
        super(MemberAddrForm, self).__init__(*args, **kwargs)


class MemberAddrNonDistanceForm(MemberAddrForm):
    class Meta:
        model = Memberaddr
        fields = ('id_member', 'addr')

