# Generated by Django 4.1.5 on 2023-04-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Satıcı'),
        ),
        migrations.AlterField(
            model_name='card',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih - Saat'),
        ),
    ]
