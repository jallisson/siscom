# Generated by Django 2.1.5 on 2019-02-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encom', '0007_auto_20190221_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='AÇAIEX'),
        ),
    ]