# Generated by Django 3.2.13 on 2023-12-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universite', '0026_remove_fakulte_fakulte_adres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolum',
            name='bolum_dekan',
        ),
        migrations.AddField(
            model_name='bolum',
            name='bolum_baskan',
            field=models.CharField(default='bolum_baskan', max_length=50),
        ),
    ]
