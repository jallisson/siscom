# Generated by Django 2.1.7 on 2019-03-28 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encom', '0041_relatorio_agencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='agencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
