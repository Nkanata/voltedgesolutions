# Generated by Django 2.2.4 on 2019-10-07 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VoltsBackEnd', '0016_auto_20191007_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items', to='VoltsBackEnd.Order'),
        ),
    ]
