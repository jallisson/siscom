# Generated by Django 2.2.1 on 2020-08-08 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encom', '0063_remove_manifesto_venda'),
    ]

    operations = [
        migrations.AddField(
            model_name='manifesto',
            name='venda',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='encom.Venda'),
        ),
    ]
