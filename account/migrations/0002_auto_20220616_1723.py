# Generated by Django 3.2.4 on 2022-06-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'supervisor'), (3, 'external_supervisor'), (4, 'coordinator'), (5, 'admin')], default=1),
        ),
    ]