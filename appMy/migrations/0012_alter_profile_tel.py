# Generated by Django 4.1.5 on 2023-05-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0011_alter_profile_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.CharField(max_length=10, verbose_name='Telefon numarası'),
        ),
    ]