#!usr/bin/python
"""Test File Web Crawler designed to find products and ratings for
   products developed and targeting seniors.
"""
import unicodecsv as csv
import re as regex
import logging as log
import datetime
from web_crawler import WebCrawler

__author__ = "Disaiah Bennett"
__version__ = "0.1"

def main():
    """Extract data from the walmart website and return the information into a csv file.
    """

    url = "https://www.walmart.com/cp/home-health-care/1005860"
    crawler = WebCrawler()
    crawler.open_log()

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

        for link in links:
            crawler.catlinks.append(link.get('href'))

        for item in category:
            head, _, _ = item.text.partition("-")
            if len(head) > 30:
                pass
            else:
                crawler.categories.append(head.replace(" ", "").replace("&", ""))

    for i, _ in enumerate(crawler.categories):
        # Set the url of the crawler [Done]
        crawler.url = crawler.catlinks[i]

        if crawler.count > 17:
            break

        print("Current Category", crawler.categories[i], "URL: ", crawler.catlinks[i])

        # Open individual CSV File [Done]
        csv_file = csv.writer(open(crawler.categories[i] + ".csv", "wb"))
        db_csv_file = csv.writer(open("db_" + crawler.categories[i] + ".csv", "wb"))
        db_csv_file_review = csv.writer(open(crawler.categories[i] + "_review.csv", "wb"))

        # Parse html data [Done]
        soup = crawler.data_extract()

        # Products to a list [Products]
        prods = soup.find_all("a", {"class": "product-title-link line-clamp line-clamp-2"})

        # Ratings [Done]
        ratings = soup.find_all("span", {"class": "seo-avg-rating"})

        # Prices [Done]
        prices = soup.find_all("div", {"class": "price-main-block"})

        # Links [Done]
        links = soup.find_all("div", {"class": ["search-result-productimage gridview", "search-result-productimage listview"]})

        for link in links:
            sub_links = link.find_all("a", {"class": "display-block"})
            for j, _ in enumerate(sub_links):
                cat_product_link.append(sub_links[j].get("href"))

        # For k in the range of products total
        for k, _ in enumerate(prods):
            try:
                rate = float(ratings[k].text)
                cat_product_rating.append(round(rate, 1))
                cat_product_price.append(prices[k].text)

                crawler.sub_url = "https://www.walmart.com" + cat_product_link[k]
                print(crawler.get_sub_url())

                sub_soup = crawler.sub_data_extract()
                #about = sub_soup.find_all("div", {"class": "about-desc"})
                about = regex.findall(r'"Product Short Description","displayValue":"(.*?)"', str(sub_soup))
                review = sub_soup.find_all("div", {"class": "collapsable-content-container"})
                product_ids = sub_soup.find_all("div", {"class": "valign-middle secondary-info-margin-right copy-mini display-inline-block wm-item-number"})
                ids = product_ids[0].text

                description = str(about).replace("[", "").replace("]", "").replace('"',"")

                for ch in ['\\','`','*','_','{','}','(',')', '<p', '<br', '<', '>','#','+','-','.','!','$','\'', 'br ']:
                    if ch in description:
                        description = description.replace(ch, "")
                csv_file.writerow([prods[k].text, cat_product_price[k], str(cat_product_rating[k]) + "/5.0", "https://www.walmart.com" + cat_product_link[k], description, ids])
                db_csv_file.writerow([prods[k].text, cat_product_price[k], str(cat_product_rating[k]) + "/5.0", "https://www.walmart.com" + cat_product_link[k], description, ids])

                for comment in review:
                    db_csv_file_review.writerow([crawler.categories[i], ids, prods[k].text, "https://www.walmart.com" + cat_product_link[k], comment.text])
                    log.info("DATA EXTRACTION [SUCCESS][%s]" % crawler.get_sub_url())

            except IndexError:
                log.warning("DATA EXTRACTION [FAILED][%s]" % crawler.get_sub_url())

        print(crawler.categories[crawler.count] + ".csv file created.")
        print("db_" + crawler.categories[crawler.count] + "_review.csv file created.")
        print(crawler.categories[crawler.count] + "_review.csv file created.\n")

        crawler.count += 1
        cat_product_price.clear()
        cat_product_link.clear()
        cat_product_rating.clear()

    crawler.cleanup()
    crawler.csv_to_database()
    crawler.log_cleanup()

if __name__ == "__main__":
    main()
