# Generated by Django 3.0.3 on 2020-09-27 21:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0006_member_field_image_udate'),
    ]

    operations = [
        migrations.AddField(
            model_name='mannerlog',
            name='reviewer',
            field=models.ForeignKey(db_column='reviewer', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='common.Member'),
        ),
        migrations.AddField(
            model_name='member',
            name='auth',
            field=models.OneToOneField(blank=True, db_column='auth', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='MannerReviewer',
        ),
    ]