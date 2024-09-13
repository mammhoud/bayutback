searchBarInput = "//input[@class='a41c4dcc FilterDesign2022 b8ab28f4']"
searchBarFindButton_Transaction = "//button[@aria-label='Find button']"
searchBarFindButton_Properties = "//a[@aria-label='Find button']"
searchBarOption_Transactions = "//button[@aria-label='Transactions']"
searchBarOption_Properties = "//button[@aria-label='Property search']"

searchBarCategory_Buy= "//button[contains(.,'Buy')]"
searchBarCategory_Rent= "//button[contains(.,'Rent')]"
searchBarInput_suggestion = "//span[@class='_0ab46ba6 FilterDesign2022']"
searchBarInput_suggestion1 = "//div[@class='_3fa626dc FilterDesign2022']//span[@class='_0ab46ba6 FilterDesign2022']"
transactionsPageDurations = "//span[@class='ef5cccac FilterDesign2022']//span[@class='bf714504']"
transactionsPageDuration_Filter = "//div//div[@class='_3f35dbb9 FilterDesign2022 _6d60a090']//li[5]"
transactionsPageTable = "//table[@class='_3336fc4e _1ec30276 _14fa9064 _4d57381b']"
transactionsPageTable_Row = ".//tbody/tr"
transactionsPageRow_Cell = ".//td"
permitNumber = "//span[@aria-label='Permit Number']"
refrenceCode = "//span[@aria-label='Reference']"
askingPrice = "//div[@class='_126656cb _2f1352a2']//span[@aria-label='Price']"
bathRooms = "//span[@aria-label='Baths']/span"
bedRooms = "//span[@aria-label='Beds']/span"
propertySize_sqft = "//span[@aria-label='Area']/span/span"
buildingName = "//span[@aria-label='Building Name']"
propertyHeader = "//div[@aria-label='Property header']"
propertyType = "//span[@aria-label='Type']"
buildUpArea = "//span[@aria-label='Built-up Area']//span[@class='b2bb77b7']/span"
addedDate = "//span[@aria-label='Reactivated date']"
completionYear= "//span[@aria-label='Year of Completion']//div[@class='a7cd24f7']"
transactionCategoryTab_Property = "//div[@class='_96aa05ec']/div[@class='e239f8ba']//h3['_4b6fd844 _13371f14']"
lastTransaction = "//ul[@class='_3ba58a89']//li[1]"
trakheesi_link = "//a[@class='_2a2779d5']"
tarkheesi_listingNumber = "//div[contains(., 'Listing Number')]/span[2]"
tarkheesi_propertySize_sqm = "//div[contains(., 'Property Size(Sqm)')]/span[2]"
###
listProperties_Page_Filter = "//span[contains(., 'TruCheck™ listings first')]"

listProperties_Page_Location = "//div[@class='_1075545d _96d4439a']//h3[@class='_00a37089']" # building Name, project Name, Area, Country 
## Create Folders with Country -> Area -> Project Name -> Building Name (json)
### add to database the values then edit it with full data scrapped 
listProperties_Page_Type = ".//div[@class='d6e81fd0']//span[@aria-label='Type']" #
listProperties_Page_Beds = ".//div[@class='d6e81fd0']//span[@aria-label='Beds']"
listProperties_Page_Baths = ".//div[@class='d6e81fd0']//span[@aria-label='Baths']"
listProperties_Page_Size_sqft = ".//div[@class='_1075545d _22b2f6ed']//h4[@class='_055807dc _4bdd430c']"
listProperties_Page_Price = ".//div[@class='d6e81fd0']//span[@aria-label='Price']"

listProperties_Page = "//ul[@class='_357a9937']/li[@class='ef447dde']"

listProperties_Page_Badge = ".//div[@aria-label='DLD History verification badge']"
listProperties_Page_Links = ".//div[@class='_4041eb80']/a" 

pageNext = "//div[@title='Next']"