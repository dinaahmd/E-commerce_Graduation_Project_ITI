# Generated by Django 4.2.2 on 2023-06-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
