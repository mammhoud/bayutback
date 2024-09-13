from django.db import models
from manage import init_django

'''
Area
Permit_Number
Building_Name
Project_Name
Property_Size_Sqft
Property_Size_(Sqm)
RoomsBaths
Link
Year_of_Completion
Built-up_Area_(Sqft)
Property_Type_(En)
Asking_Price_(AED)
REF
Instance_Date
Actual_Worth_(AED)
Trans_Group
Rent_Expiry
RentedAgency_1
Expiry_Date_1
Agency_2
Expiry_Date_2
Agency_3
Expiry_Date_3
Count_Buy
Count_Rent_Listing_Number
Name_(En)
Mobile
Unit_Number
'''


init_django()
class Property(models.Model):
    Link= models.CharField(max_length=200, null=True)
    Permit_Number = models.CharField(max_length=200, null=True)
    Area = models.CharField(max_length=200, null=True)
    Building_Name = models.CharField(max_length=200, null=True)
    Project_Name = models.CharField(max_length=200, null=True)
    Property_Size_Sqft= models.CharField(max_length=200, null=True)
    Property_Size_Sqm= models.CharField(max_length=200, null=True)
    Rooms= models.CharField(max_length=200, null=True)
    Baths= models.CharField(max_length=200, null=True)
    Year_of_Completion= models.CharField(max_length=200, null=True)
    Built_up_Area_Sqft= models.CharField(max_length=200, null=True)
    Property_Type_En= models.CharField(max_length=200, null=True)
    Asking_Price_AED= models.CharField(max_length=200, null=True)
    REF= models.CharField(max_length=200, null=True)
    Instance_Date= models.CharField(max_length=200, null=True)
    Actual_Worth_AED= models.CharField(max_length=200, null=True)
    Trans_Group= models.CharField(max_length=200, null=True)
    Rent_Expiry= models.CharField(max_length=200, null=True)
    RentedAgency_1= models.CharField(max_length=200, null=True)
    Expiry_Date_1= models.CharField(max_length=200, null=True)
    Agency_2= models.CharField(max_length=200, null=True)
    Expiry_Date_2= models.CharField(max_length=200, null=True)
    Agency_3= models.CharField(max_length=200, null=True)
    Expiry_Date_3= models.CharField(max_length=200, null=True)
    Count_Buy= models.CharField(max_length=200, null=True)
    Count_Rent_Listing_Number= models.CharField(max_length=200, null=True)
    Name_En= models.CharField(max_length=200, null=True)
    Mobile= models.CharField(max_length=200, null=True)
    Unit_Number= models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200, null=True)
    SearchQuery = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.SearchQuery + " " + self.Permit_Number


class PropertyTransaction(models.Model):
    Instance_Date = models.CharField(max_length=200, null=True)
    Area = models.CharField(max_length=200, null=True)
    Project_Name = models.CharField(max_length=200, null=True)
    Building_Name = models.CharField(max_length=200, null=True)
    Actual_Worth_AED = models.CharField(max_length=200, null=True)
    Property_Type_En = models.CharField(max_length=200, null=True)
    Rooms = models.CharField(max_length=200, null=True)
    Built_up_sqft = models.CharField(max_length=200, null=True)
    Plot_sqft = models.CharField(max_length=200, null=True)
    Unit_Number = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Unit_Number + " " + self.Built_up_sqft + " " + self.Project_Name


class PropertyListing(models.Model):

    Link= models.CharField(max_length=200, null=True)#
    Built_up_Area_Sqft= models.CharField(max_length=200, null=True)# 
    Property_Type_En= models.CharField(max_length=200, null=True)#
    Asking_Price_AED= models.CharField(max_length=200, null=True)#
    Location = models.CharField(max_length=200, null=True)#
    Baths = models.CharField(max_length=200, null=True)#
    Rooms = models.CharField(max_length=200, null=True)#
    SearchQuery = models.CharField(max_length=200, null=True)#
    def __str__(self):
        return self.SearchQuery + " " + self.Link

