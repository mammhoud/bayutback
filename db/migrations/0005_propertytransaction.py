# Generated by Django 4.1.13 on 2024-04-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_propertylisting_property_searchquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instance_Date', models.CharField(max_length=200, null=True)),
                ('Area', models.CharField(max_length=200, null=True)),
                ('Project_Name', models.CharField(max_length=200, null=True)),
                ('Building_Name', models.CharField(max_length=200, null=True)),
                ('Actual_Worth_AED', models.CharField(max_length=200, null=True)),
                ('Property_Type_En', models.CharField(max_length=200, null=True)),
                ('Rooms', models.CharField(max_length=200, null=True)),
                ('Built_up_sqft', models.CharField(max_length=200, null=True)),
                ('Plot_sqft', models.CharField(max_length=200, null=True)),
                ('Unit_Number', models.CharField(max_length=200, null=True)),
                ('Location', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
