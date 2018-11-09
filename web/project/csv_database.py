from mysql import connector
import csv
import logging as log
from web_crawler import WebCrawler

"""Extract data from the walmart website and return the information into a csv file.
"""
url = "https://www.walmart.com/cp/home-health-care/1005860"
crawler = WebCrawler()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Function
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Set the url of the crawler
crawler.url = url
soup = crawler.data_extract()

cat_product_price = []
cat_product_link = []
cat_product_rating = []

cat_sidebar_li = soup.find_all("li", {"class": "SideBarMenuModuleItem"})

for category in cat_sidebar_li:
    links = category.findAll("a", {"class": "SideBarMenu-toggle"})
    item = category.findAll("span", {"class": "SideBarMenu-title"})

    if crawler.count > 16:
        break

    for link in links:
        crawler.catlinks.append(link.get('href'))

    for item in category:
        head, _, _ = item.text.partition("-")
        if len(head) > 30:
            pass
        else:
            crawler.categories.append(head)
    crawler.count += 1

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Function [Connecting to database]
#----------------------------------------------------------------------------------------------------------------------------------------------------------
mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Web-Crawler"
)
mycursor = mydb.cursor()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Function [Create table within database, and insert the data from the csv files]
#----------------------------------------------------------------------------------------------------------------------------------------------------------
for i, category in enumerate(crawler.categories):
    table_name = category.replace(" ", "").replace("&", "")
    try:
        sql_drop = "DROP TABLE IF EXISTS %s" % table_name
        mycursor.execute(sql_drop)
    except:
        log.warning("SQL [DROP TABLE] was not executed successfully.")
        
    try:
        sql_create = "CREATE TABLE %s (Product_Name VARCHAR(200), Price VARCHAR(10), Rating VARCHAR(7), Link VARCHAR(500), About VARCHAR(10000))" % table_name
        mycursor.execute(sql_create)
    except:
        log.warning("SQL [CREATE TABLE] was not executed successfully.")

    try:
        print(i+1, ": ", "csv/" + category + ".csv")
        file_name = "csv/" + category.replace(" ", "").replace("&", "") + ".csv"
        csvdata = csv.reader(open(file_name, "r"))
        for row in csvdata:
            sql_insert = "INSERT INTO " + table_name + " (Product_Name, Price, Rating, Link, About) VALUES (%s, %s, %s, %s, %s)"
            vals = (row[0], row[1], row[2], row[3], row[4])
            mycursor.execute(sql_insert, vals)
    except:
        log.warning("SQL [INSERT] was not executed successfully.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------
