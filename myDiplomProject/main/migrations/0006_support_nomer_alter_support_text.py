# Generated by Django 5.0.3 on 2024-03-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_grade_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='nomer',
            field=models.IntegerField(default=1, verbose_name='Ваш номер(без плюса)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='support',
            name='text',
            field=models.TextField(verbose_name='Ваша проблема'),
        ),
    ]