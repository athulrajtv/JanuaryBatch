# Generated by Django 4.1.7 on 2023-03-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(blank=True, max_length=40, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('Image', models.ImageField(blank=True, max_length=40, null=True, upload_to='')),
            ],
        ),
    ]
