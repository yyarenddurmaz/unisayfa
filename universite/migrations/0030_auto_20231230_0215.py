# Generated by Django 3.2.13 on 2023-12-30 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universite', '0029_auto_20231229_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolum',
            name='bolum_fırsat',
        ),
        migrations.AddField(
            model_name='bolum',
            name='bolum_firsat',
            field=models.TextField(default='bolum_firsat', max_length=400),
        ),
    ]
