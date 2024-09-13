from utils.dateValidations import *
from elements import *
from utils.webDriver import webDriver
import pandas as pd
import utils.save_Data as save_Data
from utils.load_File import find_row_with_least_null_values as notNullRow
from db.models import *
import scrapPDF



def propertyDetails(driver: webDriver,propertiesListFilter, withUnitNumber: bool = True) -> None:
    """
    Prompts the user to choose their data needs and performs the corresponding actions.
    """
    print("|________________________________|")
    print("|----------------|")
    print("|Please Wait ....|")
    print("|----------------|")
    time.sleep(1)
    scrappedLinks = []
    for item in propertiesListFilter:
        if item not in scrappedLinks:
            scrappedLinks.append(item)    
            pass
        else:
            continue
        
        agency1 = "NA"
        agency2 = "NA"
        agency3 = "NA"
        expire_date1 = "NA"
        expire_date2 = "NA"
        expire_date3 = "NA"
        count_Buy= 0
        count_Rent =0
        builtUp_Area = " sqft"
        year_of_Completion = None 
        header = None 
        type_ = None
        permit_Number = None 
        building_Name = None 
        propertyArea_size = " sqft" 
        beds = None 
        baths = None 
        currency = None 
        last_transaction_buy_Type = "NA"
        last_transaction_buy_Date = "NA"
        last_transaction_buy_price = "NA"
        last_transaction_rent_price = "NA"
        last_transaction_rent_Date = "NA"
        reference_code = None 
        transaction = []            
        is_buy = True
        is_rent = True
        is_else= True
        driver.get(item)
        update_date = datetime.strptime('31/12/2018', '%d/%m/%Y')
        transaction = []
        transaction_rent=["NA","NA","NA"]
        transaction_buy=["NA","NA","NA"]
        try:    
            reactivated_date = driver.element(addedDate).text
            reactivated_date = reactivated_date.split(" ")[0] + " "+ reactivated_date.split(" ")[1][:3] + " "+ reactivated_date.split(" ")[2]
            reactivated_date = change_date_format(reactivated_date)
            if (datetime.strptime(reactivated_date, '%d/%m/%Y') - update_date) < timedelta(days=1):
                continue
        except Exception as e:
            print(f"The elements was not found within the li element: {str(e)}")

        try:
            time.sleep(2)
            permit_Number = driver.element(permitNumber).text
            print("|________________________________|")

            print(f"Current Listing Permit Number: {permit_Number}")

            if driver.element(transactionCategoryTab_Property):
                elems = driver.findElements(transactionCategoryTab_Property)
                for ell in elems:
                    ell.click()
                    try: 
                        transaction = driver.element(lastTransaction).text.split('\n')
                    except:
                        print("this property dosnt have any transaction sale history...")
                        continue
                    transaction_temp = []
                    if len(transaction) != 0:
                        if transaction[1].lower() not in ('rent','sale'):  
                            transaction_temp.append("RENT")
                            transaction_temp += transaction
                            transaction_temp[2] = transaction_temp[2].replace('Active','')
                            transaction_rent = transaction_temp
                        else:
                            transaction_temp.append("SALE")
                            transaction_temp += transaction
                            transaction_temp.remove('Sale')
                            transaction_buy = transaction_temp

            try:
                last_transaction_buy_Type = transaction_buy[0]
                last_transaction_buy_price = transaction_buy[3] + " " +  transaction_buy[2]
                last_transaction_buy_Date = transaction_buy[1]

                last_transaction_buy_Date = change_date_format(last_transaction_buy_Date)

                
            except:
                last_transaction_buy_Type = "NA"
                last_transaction_buy_price = "NA"
                last_transaction_buy_Date = "NA"
                is_buy = False
            try:
                last_transaction_rent_Date = transaction_rent[2]
                last_transaction_rent_price = transaction_rent[4] + " " +  transaction_rent[3]
                last_transaction_rent_Date = change_date_format(last_transaction_rent_Date)

            except:
                last_transaction_rent_Date = "NA"
                last_transaction_rent_price = "NA"
                is_rent = False
                
            if last_transaction_buy_Date != "NA":
                date_buy_ch = datetime.strptime(last_transaction_buy_Date, '%d/%m/%Y')
            if  last_transaction_rent_Date != "NA" :
                date_rent_ch = datetime.strptime(last_transaction_rent_Date, '%d/%m/%Y')
            if is_buy and is_rent:
                if date_buy_ch > date_rent_ch:
                    if (date_buy_ch - update_date) < timedelta(days=1):
                        is_else = True
                    else:
                        is_else = False
                    is_rent=False
                elif date_buy_ch < date_rent_ch:
                    if (date_rent_ch - update_date) < timedelta(days=1):
                        is_else = True
                    else:
                        is_else = False
                    is_buy=False
                else:
                    is_buy = False
                    is_rent=False
            elif is_buy:
                is_rent = False
            elif is_rent:
                is_buy = False
            year_of_Completion = driver.element(completionYear).text
            builtUp_Area = driver.element(buildUpArea).text
            header = driver.element(propertyHeader).text

            if ' | ' in header:
                header = header.replace(' | ', ', ')
            sheader = header.split(', ')
            type_ = driver.element(propertyType).text
            building_Name = driver.element(buildingName).text
            propertyArea_size = driver.element(propertySize_sqft).text
            try:
                beds = driver.element(bedRooms).text
            except:
                beds = 'NA'
            baths = driver.element(bathRooms).text
            currency = driver.element(askingPrice).text
            reference_code = driver.element(refrenceCode).text
        except Exception as e:
            print("", e)
            print("error while extract one of elements  _",e)
        
        property_size = "Not found -> sqft"
        
        pArea = sheader[1]
        pName= sheader[0]
        properitySize = propertyArea_size.replace(' sqft','')
        actualW = last_transaction_buy_price.replace(' AED','')
        builtUpArea= builtUp_Area.index('sqft')
        builtUpArea=builtUp_Area[:builtUpArea].strip()
        print(" _____> ",builtUpArea)
        beds = beds.replace(' Beds','')
        baths = baths.replace(' Baths','')
        matched_transaction = "NA"
        if withUnitNumber:
            if is_buy:
                matched_transaction = PropertyTransaction.objects.filter(Actual_Worth_AED = actualW, Built_up_sqft__contains = builtUpArea, Instance_Date=last_transaction_buy_Date,Location__contains=pArea).first()
                if matched_transaction:
                    print("matched_transaction",matched_transaction)
                    print("last_transaction_buy_Date",last_transaction_buy_Date  + "  ->  "+ matched_transaction.Instance_Date)
                    print("Actual_Worth_AED",actualW + "  ->  "+ matched_transaction.Actual_Worth_AED)
                    print("Unit_Number" + "  ->  "+ matched_transaction.Unit_Number)
                    matched_transaction= matched_transaction.Unit_Number

        
        try:

            driver.wait_for_element(trakheesi_link)
            link_element = driver.element(trakheesi_link)
            href = link_element.get_attribute("href")
            driver.get(href)

            link_element = driver.wait_for_element(tarkheesi_propertySize_sqm)
            property_size_sqm = driver.element(tarkheesi_propertySize_sqm).text
        except Exception as e:
            print("Values Not found,",e)



        try:
            driver, agency1,agency2,agency3,expire_date1,expire_date2,expire_date3 = scrapPDF.pdfProcessing(driver, permit_Number)
        except Exception as e:
            print("Values Not found,",e)



        nameEn,mobilePhone,inputUnit = detailsFromInputData(matched_transaction, property_size_sqm)
            
        save_Data.saveObject(pd.DataFrame([{
                                "Link" :  item,
                                "Permit_Number " :  permit_Number,
                                "Area " :  pArea,
                                "Building_Name " :  building_Name,
                                "Project_Name " :  pName,
                                "Property_Size_Sqft" :  properitySize,
                                "Property_Size_Sqm" :  property_size_sqm,
                                "Rooms" :  beds,
                                "Baths" :  baths,
                                "Year_of_Completion" :  year_of_Completion,
                                "Built_up_Area_Sqft" :  builtUpArea,
                                "Property_Type_En" :  type_,
                                "Asking_Price_AED" :  currency,
                                "REF" :  reference_code,
                                "Instance_Date" :  last_transaction_buy_Date,
                                "Actual_Worth_AED" :  actualW,
                                "Trans_Group" :  last_transaction_buy_Type,
                                "Rent_Expiry" :  last_transaction_rent_Date,
                                "RentedAgency_1" :  agency1,
                                "Expiry_Date_1" :  expire_date1,
                                "Agency_2" :  agency2,
                                "Expiry_Date_2" :  expire_date2,
                                "Agency_3" :  agency3,
                                "Expiry_Date_3" :  expire_date3,
                                "Count_Buy" :  count_Buy,
                                "Count_Rent_Listing_Number" :  count_Rent,
                                "Name_En" :  nameEn,
                                "Mobile" :  mobilePhone,
                                "Unit_Number" :  matched_transaction,
                                "Location " :  header,
                                }])
                ,pArea,
                function="PropertisListing"
        )
        print("------------------------------------------------------------------------------------------------")
    return driver


def detailsFromInputData(unumber, sizeSqm):



    try:
        df = pd.read_excel('db/Files/(InputData).xlsx')

        # Define the column you want to search in
        search_column_1  = 'UnitNumber'
        search_column_2 = 'Size'
        # Define the value you want to search for
        search_value_1  = unumber
        search_value_2 = sizeSqm


        search_results = df[(df[search_column_1] == search_value_1) & (df[search_column_2] == search_value_2)]
        search_results = notNullRow(search_results)

        return search_results['NameEn'], search_results['Mobile'], search_results['UnitNumber']
    except Exception as e:
        print("Values Not found,",e)
        return "NA","NA","NA"



if __name__ == "__main__":
    driver = webDriver()
    list=[ "https://www.bayut.com/property/details-8598105.html","https://www.bayut.com/property/details-8066619.html"]
    propertyDetails(driver, list)