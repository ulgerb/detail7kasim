# Generated by Django 4.1.5 on 2023-05-05 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0009_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMy.brand', verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı - Satıtcı'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=50, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='profile', verbose_name='Profil Resmi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, default='-', max_length=50, verbose_name='Meslek'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.CharField(blank=True, default='-', max_length=10, verbose_name='Telefon numarası'),
        ),
    ]
