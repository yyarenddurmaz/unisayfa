# Generated by Django 3.2.13 on 2023-11-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universite', '0011_bolum_fakulte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakulte',
            name='fakulte_ad',
            field=models.CharField(default='fakulte', max_length=50),
        ),
    ]
