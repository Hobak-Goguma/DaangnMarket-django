# Generated by Django 3.0.3 on 2020-08-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorycode',
            name='code',
            field=models.CharField(choices=[('ELECTRONICS', '디지털/가전'), ('FURNITURE', '가구/인테리어'), ('INFANT', '유아동/유아도서'), ('DAILY', '생활/가공식품'), ('SPORTS', '스포츠/레저'), ('WOMEN-GOODS', '여성잡화'), ('WOMEN-FASHION', '여성의류'), ('MEN', '남성팬션/잡화'), ('GAME', '게임/취미'), ('BEAUTY', '뷰티/미용'), ('PET', '반려동물용품'), ('CULTURE', '도서/티켓/음반'), ('ETC', '기타 중고물품'), ('LOCAL_SHOP', '동네업체 소개')], db_column='code', default='ETC', max_length=30, primary_key=True, serialize=False),
        ),
    ]