# Generated by Django 3.1.5 on 2021-01-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210121_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_added',
            field=models.DateTimeField(verbose_name='data publicação'),
        ),
    ]
