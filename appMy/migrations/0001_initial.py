# Generated by Django 4.1.5 on 2023-04-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='İçerik')),
                ('date_now', models.DateTimeField(verbose_name='Tarih - Saat')),
                ('image', models.ImageField(max_length=200, upload_to='cards', verbose_name='Resim')),
                ('author', models.CharField(max_length=50, verbose_name='Yazar')),
            ],
        ),
    ]