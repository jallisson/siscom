# Generated by Django 2.1.7 on 2019-03-21 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encom', '0030_auto_20190315_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='valor_nota',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Valor Nota'),
        ),
    ]
