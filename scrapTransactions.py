from utils.dateValidations import *
from elements import *
from utils.webDriver import webDriver
import pandas as pd
import utils.save_Data as save_Data


def transactionTable(driver: webDriver,):

    driver.click(transactionsPageDurations)
    driver.click(transactionsPageDuration_Filter)
    time.sleep(3)    
    driver.wait_for_element(transactionsPageTable)
    
    while True:
        table = driver.element(transactionsPageTable)

        # Iterate through table rows
        rows = driver.findElements(transactionsPageTable_Row,table)
        for row in rows:
            cells = driver.findElements(transactionsPageRow_Cell,row)
            try:
                if cells[0]:
                    date = cells[0].text.strip().replace('\n', ' ')
                    date = change_date_format(date)
                    location = cells[1].text.strip().replace('\n', ', ')
                    price = cells[2].text.strip()
                    prop_type = cells[3].text.strip()
                    beds = cells[4].text.strip()
                    built_up = cells[5].text.strip()
                    plot = cells[6].text.strip()
                    unit = cells[7].text.strip()
                    Project_Name = location.split(', ')[0]
                    Building_Name = location.split(', ')[-1]
                    try:
                        Area = location.split(', ')[1]
                    except:
                        Area = ""
                    obj = {
                        "Instance_Date": date,
                        "Area": Area,
                        "Project_Name": Project_Name,
                        "Building_Name": Building_Name,
                        "Actual_Worth_AED": price,
                        "Property_Type_En": prop_type,
                        "Rooms": beds,
                        "Built_up_sqft": built_up,
                        "Plot_sqft": plot,
                        "Unit_Number": unit,
                        "Location": location
                    }
                    # df = pd.DataFrame(obj)
                    # save_File.saveObject(df,location.split(', ')[-1],function="transactionTable")
                    save_Data.saveObjectsToDatabase(obj,"PropertyTransaction")

            except:
                break
        # pageNext = driver.element(transactionsPageNext)
        if not driver.click(pageNext):
            break
        else:
            print("Next Page")
    return driver




if __name__ == "__main__":
    driver = webDriver()
    driver.get("https://www.bayut.com/property-market-analysis/sale/dubai/downtown-dubai/29-boulevard/")
    transactionTable(driver)
    driver.close()
    driver.quit()