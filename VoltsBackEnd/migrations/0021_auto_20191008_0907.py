# Generated by Django 2.2.4 on 2019-10-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoltsBackEnd', '0020_auto_20191007_0707'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RefOrderItemStatusCode',
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('date_order_placed',)},
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]