# Generated by Django 2.2.4 on 2019-09-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoltsBackEnd', '0003_auto_20190920_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsubcategory',
            name='subcategory_photo',
            field=models.ImageField(blank=True, upload_to='card-categories-images/', verbose_name='image on the homepage categories'),
        ),
    ]
