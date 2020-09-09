# Generated by Django 3.0.3 on 2020-09-04 03:45

import imagekit.models.fields
from django.db import migrations, models

import common.models.member_model


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_member_field_add_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=common.models.member_model.Member.upload_to_id_image),
        ),
        migrations.AlterField(
            model_name='member',
            name='udate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]