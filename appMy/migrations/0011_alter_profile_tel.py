# Generated by Django 4.1.5 on 2023-05-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0010_alter_card_brand_alter_card_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.CharField(default='-', max_length=10, verbose_name='Telefon numarası'),
        ),
    ]
