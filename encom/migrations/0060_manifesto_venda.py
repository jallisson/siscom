# Generated by Django 2.2.1 on 2020-08-06 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encom', '0059_auto_20200728_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='manifesto',
            name='venda',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='encom.Venda'),
        ),
    ]