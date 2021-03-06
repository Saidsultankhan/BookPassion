# Generated by Django 3.1.7 on 2021-05-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210522_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(verbose_name='В наличии шт'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
    ]
