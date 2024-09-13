import scrapProperties, scrapTransactions, searchFields
import searchPropertiesListing
from scrapTransactions import transactionTable
from db.models import *
from utils.webDriver import *
from utils.dateValidations import *



def main(driver, Location,propertiesFor= "Buy",srapWithTransactions = False,specifiedSearch = "", searchFor= "transactions"):

    if srapWithTransactions:
        # driver = searchFields.search(driver, Location= Location, propertiesFor = propertiesFor,searchFor = "Transactions",)

        # driver = scrapTransactions.transactionTable(driver)
        driver.get("https://www.bayut.com/")

        # driver = searchFields.search(driver, Location= Location, propertiesFor = propertiesFor,searchFor = "propert",)
        # driver = searchPropertiesListing.listingLinks(driver)
        if specifiedSearch:
            propertiesListFilter = PropertyListing.objects.filter(Location__contains=Location, SearchQuery__contains=specifiedSearch).distinct().values_list('Link', flat=True)
        else:
            propertiesListFilter = PropertyListing.objects.filter(Location__contains=Location).distinct().values_list('Link', flat=True)
        driver = scrapProperties.propertyDetails(driver,propertiesListFilter)

        driver = scrapProperties.propertyDetails(driver,propertiesListFilter)

    else:
        driver = searchFields.search(driver, Location= Location, propertiesFor = propertiesFor,searchFor = searchFor,)
        if "trans" in searchFor.lower():
            driver = scrapTransactions.transactionTable(driver)
        else:
            driver = searchPropertiesListing.listingLinks(driver)
            if specifiedSearch:
                propertiesListFilter = PropertyListing.objects.filter(Location__contains=Location, SearchQuery__contains=specifiedSearch).distinct().values_list('Link', flat=True)
            else:
                propertiesListFilter = PropertyListing.objects.filter(Location__contains=Location).distinct().values_list('Link', flat=True)
            driver = scrapProperties.propertyDetails(driver,propertiesListFilter)


    # list = []
    # for a in propertiesListFilter:
    #     if a.Link not in list:
    #         list.append(a.Link)
    #         print(a.Link)
    return driver


if __name__ == "__main__":
    driver = webDriver()
    driver.get("https://www.bayut.com/")
    driver = main(driver, "The Address Residences Dubai", "buy", searchFor="propert",srapWithTransactions = True)
    driver.quit()

    # propertiesListFilter = Property.objects.filter(Location__contains="29 Boulevard")
    # list = []
    # for a in propertiesListFilter:
    #     list.append(a.Link)

    # scrapProperties.propertyDetails(driver,list)

