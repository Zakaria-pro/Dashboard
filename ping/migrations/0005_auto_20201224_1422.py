# Generated by Django 3.1.4 on 2020-12-24 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0004_auto_20201224_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='ip_adr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ping.network', verbose_name='Id_Ip'),
        ),
    ]
