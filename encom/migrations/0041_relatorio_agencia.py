# Generated by Django 2.1.7 on 2019-03-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('encom', '0040_remove_relatorio_agencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorio',
            name='agencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
