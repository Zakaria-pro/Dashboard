# Generated by Django 3.1.4 on 2020-12-25 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0007_auto_20201225_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='ip_adr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ping.network', verbose_name="Id de l'adresse Ip"),
        ),
    ]
