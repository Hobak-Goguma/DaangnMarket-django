# Generated by Django 3.0.3 on 2020-08-31 18:23

import django.db.models.deletion
import imagekit.models.fields
from django.db import migrations, models

import posts.models.company_image_model


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_product_image_and_company_rename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='img',
        ),
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.ForeignKey(db_column='code', default='ETC', on_delete=django.db.models.deletion.DO_NOTHING, to='posts.CategoryCode'),
        ),
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(default='', max_length=50)),
                ('image', imagekit.models.fields.ProcessedImageField(null=True, upload_to=posts.models.company_image_model.CompanyImage.upload_to_id_image)),
                ('id_company', models.ForeignKey(db_column='id_company', on_delete=django.db.models.deletion.CASCADE, related_name='thum', to='posts.Company')),
            ],
            options={
                'db_table': 'company_image',
            },
        ),
    ]