# Generated by Django 4.1.5 on 2023-04-14 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_alter_card_author_alter_card_date_now'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Marka')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.brand', verbose_name='Marka'),
        ),
    ]