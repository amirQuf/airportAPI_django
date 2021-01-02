# Generated by Django 3.1.3 on 2021-01-02 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0002_auto_20210102_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest', to='airport.airport', verbose_name='مقصد'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='orgin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='airport.airport', verbose_name='مبدا'),
        ),
    ]
