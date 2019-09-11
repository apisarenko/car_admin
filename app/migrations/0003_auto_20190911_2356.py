# Generated by Django 2.1.1 on 2019-09-11 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_review_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-id'], 'verbose_name': 'Автомашина', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Обзорные статьи'},
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='review',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Car', verbose_name='Автомобиль'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
    ]