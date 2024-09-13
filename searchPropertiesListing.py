from utils.webDriver import webDriver
from elements import *
import pandas as pd
import os
from utils.dateValidations import *
import utils.save_Data as save_Data

def search_ToLinks(driver: webDriver):
    
    driver.wait_for_element(listProperties_Page_Filter)
    driver.click(listProperties_Page_Filter)
    return driver

def listingLinks(driver: webDriver, isAll=False):
        pageCount = 1
        time.sleep(2)
        SearchQuery =driver().title
        print(SearchQuery)
        while True:
            try:
                all_li_elements = driver.wait_for_element(listProperties_Page)

                for li_element in all_li_elements:
                    if driver.element(listProperties_Page_Badge,li_element) or isAll:
                        a_element = driver.element(listProperties_Page_Links,li_element)
                        property_type = driver.element(listProperties_Page_Type,li_element).text
                        try:
                            Rooms = driver.element(listProperties_Page_Beds,li_element).text
                        except Exception as e:
                            Rooms = "NA"
                        baths = driver.element(listProperties_Page_Baths,li_element).text
                        size =  driver.element(listProperties_Page_Size_sqft,li_element).text
                        price = driver.element(listProperties_Page_Price,li_element).text # listProperties_Page_Location
                        location = driver.element(listProperties_Page_Location,li_element).text# listProperties_Page_Location
                        link = a_element.get_attribute('href')
                        obj = {
                            "Link" :  link,
                            "Rooms" :  Rooms,
                            "Baths" :  baths,
                            "Built_up_Area_Sqft" :  size,
                            "Property_Type_En" :  property_type,
                            "Asking_Price_AED" :  price,
                            "Location" :  location,
                            "SearchQuery" : SearchQuery}
                        save_Data.saveObjectsToDatabase(obj, tableName="PropertyListing")
                    else:

                        pass
            except Exception as e:
                print(e)
            try:
                if not driver.click(pageNext):
                    break
                else: 
                    pageCount += 1
                    print("Page -->", pageCount)
            except Exception as e:
                print("Search & Listing Links --> Sucssesfully")
                break
            time.sleep(1)
        return driver

if __name__ =="__main__":
    driver = webDriver()
    driver.get("https://www.bayut.com/to-rent/property/dubai/downtown-dubai/?sort=verified")
    # search_ToLinks(driver)

    listingLinks(driver)
    print("Done")
    driver.close()
    driver.quit()