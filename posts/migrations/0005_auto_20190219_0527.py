# Generated by Django 2.1.7 on 2019-02-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190219_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=2200),
        ),
    ]
