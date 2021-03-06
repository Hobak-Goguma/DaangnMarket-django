# Generated by Django 3.0.3 on 2020-08-24 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200824_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manner',
            fields=[
                ('id_manner', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('udate', models.DateTimeField(auto_now=True)),
                ('id_member', models.ForeignKey(db_column='id_member', on_delete=django.db.models.deletion.DO_NOTHING, to='common.Member')),
            ],
            options={
                'db_table': 'manner',
            },
        ),
        migrations.CreateModel(
            name='MannerLog',
            fields=[
                ('id_manner_log', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('id_manner', models.ForeignKey(db_column='id_manner', on_delete=django.db.models.deletion.DO_NOTHING, to='common.Manner')),
            ],
            options={
                'db_table': 'manner_log',
            },
        ),
        migrations.CreateModel(
            name='MannerReviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_manner_log', models.ForeignKey(db_column='id_manner_log', on_delete=django.db.models.deletion.DO_NOTHING, to='common.MannerLog')),
                ('reviewer', models.ForeignKey(db_column='reviewer', on_delete=django.db.models.deletion.DO_NOTHING, to='common.Member')),
            ],
            options={
                'db_table': 'manner_reviewer',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id_log', models.AutoField(primary_key=True, serialize=False)),
                ('search', models.CharField(max_length=60)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('id_member', models.ForeignKey(db_column='id_member', on_delete=django.db.models.deletion.DO_NOTHING, to='common.Member')),
            ],
            options={
                'db_table': 'log',
            },
        ),
    ]
