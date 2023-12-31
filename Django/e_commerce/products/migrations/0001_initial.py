# Generated by Django 4.2.2 on 2023-06-30 22:34


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('slug', models.SlugField(unique=True)),
                ('discount_rate', models.PositiveIntegerField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_items', to='products.productcategory')),
                ('promotion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promotion_items', to='products.promotion')),
            ],
        ),
    ]
