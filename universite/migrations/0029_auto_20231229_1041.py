# Generated by Django 3.2.13 on 2023-12-29 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universite', '0028_auto_20231229_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bolum',
            old_name='kisaltma',
            new_name='bolum_kisaltma',
        ),
        migrations.RenameField(
            model_name='fakulte',
            old_name='kisaltma',
            new_name='fakulte_kisaltma',
        ),
    ]
