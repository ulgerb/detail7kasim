# Generated by Django 4.1.5 on 2023-05-03 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0008_card_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='Adres')),
                ('tel', models.CharField(max_length=10, verbose_name='Telefon numarası')),
                ('job', models.CharField(max_length=50, verbose_name='Meslek')),
                ('image', models.ImageField(max_length=255, upload_to='profile', verbose_name='Profil Resmi')),
                ('password', models.CharField(max_length=50, verbose_name='Şifre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Adı')),
            ],
        ),
    ]
