# Generated by Django 3.1.5 on 2021-01-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_added',
            field=models.DateTimeField(verbose_name='data de publicação'),
        ),
    ]
