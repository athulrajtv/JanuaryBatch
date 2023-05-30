# Generated by Django 4.1.7 on 2023-03-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Description', models.CharField(blank=True, max_length=40, null=True)),
                ('Image', models.ImageField(blank=True, max_length=40, null=True, upload_to='')),
            ],
        ),
    ]
