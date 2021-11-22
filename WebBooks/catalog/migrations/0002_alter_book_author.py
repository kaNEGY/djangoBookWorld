# Generated by Django 3.2.7 on 2021-10-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора книги', to='catalog.Authors', verbose_name='Автор книги'),
        ),
    ]
