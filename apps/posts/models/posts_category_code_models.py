from django.db import models
from django.utils.translation import gettext_lazy as _


# TextXhoices에 대해 django에서 찾아보세여! 상태에 보통 쓰인다고 해서 도입함.
class CategoryCode(models.Model):
    class CATEGORY(models.TextChoices):
        PRODUCT = 'PRODUCT', _('Product')
        PROMOTION = 'PROMOTION', _('Promotion')

    class CODE(models.TextChoices):
        ELECTRONICS = 'ELECTRONICS', '디지털/가전'
        FURNITURE = 'FURNITURE', '가구/인테리어'
        INFANT = 'INFANT', '유아동/유아도서'
        DAILY = 'DAILY', '생활/가공식품'
        SPORTS = 'SPORTS', '스포츠/레저'
        WOMEN_GOODS = 'WOMEN-GOODS', '여성잡화'
        WOMEN_FASHION = 'WOMEN-FASHION', '여성의류'
        MEN = 'MEN', '남성팬션/잡화'
        GAME = 'GAME', '게임/취미'
        BEAUTY = 'BEAUTY', '뷰티/미용'
        PET = 'PET', '반려동물용품'
        CULTURE = 'CULTURE', '도서/티켓/음반'
        ETC = 'ETC', '기타 중고물품'

    category: CATEGORY = models.CharField(max_length=20, choices=CATEGORY.choices, default=CATEGORY.PRODUCT)
    code: CODE = models.CharField(max_length=20, primary_key=True, db_column='code',
                                  choices=CODE.choices, default=CODE.ETC)

    class Meta:
        db_table = 'posts_category_code'
        app_label = 'posts'
