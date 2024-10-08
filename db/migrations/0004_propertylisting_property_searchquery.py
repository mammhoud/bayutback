# Generated by Django 4.1.13 on 2024-04-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_property_actual_worth_aed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.CharField(max_length=200, null=True)),
                ('Built_up_Area_Sqft', models.CharField(max_length=200, null=True)),
                ('Property_Type_En', models.CharField(max_length=200, null=True)),
                ('Asking_Price_AED', models.CharField(max_length=200, null=True)),
                ('Location', models.CharField(max_length=200, null=True)),
                ('Baths', models.CharField(max_length=200, null=True)),
                ('Rooms', models.CharField(max_length=200, null=True)),
                ('SearchQuery', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='SearchQuery',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
