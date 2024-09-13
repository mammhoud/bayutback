from datetime import datetime
import os
import json
import pandas as pd
from db.models import Property,PropertyListing,PropertyTransaction

def saveObject(object,proj,append= False, file_name =  None, function = "listingLinks"):
    file_Path = os.path.join('db/Files',proj,)
    try:
        os.makedirs(file_Path)
    except Exception as e:
        print()
    finally:
        name_prefix = f'{datetime.now().strftime("%m-%Y")}'
        file_name = name_prefix +  f" ({function}).csv"  # Default file name

        file_Name = os.path.join(file_Path, file_name)
        print(os.listdir(file_Path))
        if os.access(file_Name, os.R_OK):
            object.to_csv(file_Name, mode='a', index=False, header=False)
        else:
            object.to_csv(file_Name, mode='w', index=False, header=True)
        print("Saving file: ", file_Name)   


def saveObjectsToDatabase(object, tableName = "Property"):
    if tableName == "Property":
        Property.objects.create(
            
        Link=object["Link"] ,
        Permit_Number =object["Permit_Number"] ,
        Area =object["Area"] ,
        Building_Name =object["Building_Name"] ,
        Project_Name =object["Project_Name"] ,
        Property_Size_Sqft=object["Property_Size_Sqft"] ,
        Property_Size_Sqm=object["Property_Size_Sqm"] ,
        Rooms=object["Rooms"] ,
        Baths=object["Baths"] ,
        Year_of_Completion=object["Year_of_Completion"] ,
        Built_up_Area_Sqft=object["Built_up_Area_Sqft"] ,
        Property_Type_En=object["Property_Type_En"] ,
        Asking_Price_AED=object["Asking_Price_AED"] ,
        REF=object["REF"] ,
        Instance_Date=object["Instance_Date"] ,
        Actual_Worth_AED=object["Actual_Worth_AED"] ,
        Trans_Group=object["Trans_Group"] ,
        Rent_Expiry=object["Rent_Expiry"] ,
        RentedAgency_1=object["RentedAgency_1"] ,
        Expiry_Date_1=object["Expiry_Date_1"] ,
        Agency_2=object["Agency_2"],
        Expiry_Date_2=object["Expiry_Date_2"] ,
        Agency_3=object["Agency_3"] ,
        Expiry_Date_3=object["Expiry_Date_3"] ,
        Count_Buy=object["Count_Buy"] ,
        Count_Rent_Listing_Number=object["Count_Rent_Listing_Number"] ,
        Name_En=object["Name_En"] ,
        Mobile=object["Mobile"] ,
        Unit_Number=object["Unit_Number"] ,
        Location =object["Location"] ,)
    elif tableName == "PropertyTransaction":
        PropertyTransaction.objects.create(
        
        Instance_Date = object["Instance_Date"] ,
        Area = object["Area"] ,
        Project_Name = object["Project_Name"] ,
        Building_Name = object["Building_Name"] ,
        Actual_Worth_AED = object["Actual_Worth_AED"] ,
        Property_Type_En = object["Property_Type_En"] ,
        Rooms = object["Rooms"] ,
        Built_up_sqft = object["Built_up_sqft"] ,
        Plot_sqft = object["Plot_sqft"] ,
        Unit_Number = object["Unit_Number"] ,
        Location = object["Location"])

    else:
        PropertyListing.objects.create( 
        Link=object["Link"] ,
        Built_up_Area_Sqft=object["Built_up_Area_Sqft"] ,
        Property_Type_En=object["Property_Type_En"] ,
        Asking_Price_AED=object["Asking_Price_AED"] ,
        Location =object["Location"] ,
        Baths=object["Baths"] ,
        Rooms=object["Rooms"] ,
        SearchQuery=object["SearchQuery"])



if __name__ == "__main__":
    object = {
                "Link" :  "linklllllllll",
                "Permit_Number" :  '122121',
                "Area" :  None,
                "Building_Name" :  None,
                "Project_Name" :  None,
                "Property_Size_Sqft" :  None,
                "Property_Size_Sqm" :  None,
                "Rooms" :  "12312",
                "Baths" :  "1232",
                "Year_of_Completion" :  None,
                "Built_up_Area_Sqft" :  "123123",
                "Property_Type_En" :  "property",
                "Asking_Price_AED" :  "12111212121212121",
                "REF" :  None,
                "Instance_Date" :  None,
                "Actual_Worth_AED" :  None,
                "Trans_Group" :  None,
                "Rent_Expiry" :  None,
                "RentedAgency_1" :  None,
                "Expiry_Date_1" :  None,
                "Agency_2" :  None,
                "Expiry_Date_2" :  None,
                "Agency_3" :  None,
                "Expiry_Date_3" :  None,
                "Count_Buy" :  None,
                "Count_Rent_Listing_Number" :  None,
                "Name_En" :  None,
                "Mobile" :  None,
                "Unit_Number" :  None,
                "Location" :  "51",
                }

    saveObject(object, "PropertyListing")