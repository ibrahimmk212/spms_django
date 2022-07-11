# Generated by Django 3.2.4 on 2022-07-11 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_session_published'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Session', to='institute.session'),
            preserve_default=False,
        ),
    ]