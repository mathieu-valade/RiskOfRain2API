# Generated by Django 2.1.7 on 2019-05-14 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='icon',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
    ]
