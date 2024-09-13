from utils.webDriver import webDriver
from elements import *
from utils.dateValidations import *


def search(driver : webDriver, Location : str, propertiesFor : str, searchFor="Properties"):

    driver.send_text(searchBarInput, Location)
    time.sleep(4)

    driver.sendEnter(searchBarInput)
    
    # query = driver.actualElement([searchBarInput_suggestion1,searchBarInput_suggestion])
    # print("Query: ",query.text)

    if "proper" in searchFor.lower():
        driver.click(xpathValue=searchBarOption_Properties)
    else:
        driver.click(xpathValue=searchBarOption_Transactions)
    if "rent" in propertiesFor.lower():
        driver.click(xpathValue=searchBarCategory_Rent)
    else:
        driver.click(xpathValue=searchBarCategory_Buy) 
    
    
    # driver.element("//span[@aria-label='Filter label']").text

    if "proper" in searchFor.lower():
        if driver.click(searchBarFindButton_Properties):
            print("Search Done")

    else: 
        if driver.click(searchBarFindButton_Transaction):
            print("Search Done")
    return driver


if __name__ == "__main__":
    driver = webDriver()
    driver.get("https://www.bayut.com/")
    search(driver, "Downtown", "rent", "transactions")
    print("Done")

    driver.close()