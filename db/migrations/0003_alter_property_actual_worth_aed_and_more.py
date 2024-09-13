# Generated by Django 5.0.4 on 2024-04-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_rename_roomsbaths_property_baths_property_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='Actual_Worth_AED',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Agency_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Agency_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Area',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Asking_Price_AED',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Baths',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Building_Name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Built_up_Area_Sqft',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Count_Buy',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Count_Rent_Listing_Number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Expiry_Date_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Expiry_Date_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Expiry_Date_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Instance_Date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Mobile',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Name_En',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Permit_Number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Project_Name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Property_Size_Sqft',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Property_Size_Sqm',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Property_Type_En',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='REF',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Rent_Expiry',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='RentedAgency_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Rooms',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Trans_Group',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Unit_Number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='Year_of_Completion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]