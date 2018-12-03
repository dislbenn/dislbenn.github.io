#!usr/bin/python
"""Web Crawler designed to find products and ratings for products developed and targeting seniors.
"""
import os
import logging as log
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

__author__ = "Disaiah Bennett"
__version__ = "0.1"

class WebCrawler:
    """Web Crawler
    """
    def __init__(self, url=None, about=None, sub_url=None, page=None, data=None, clean=False):
        """This is the inside of my web crawler
            url: string - the url
            about: string - product description
            sub_url: string - sub url
            page: object - the url page.
            data: object - the page data.
            categories: list - navigation categories
            catlinks: list - navigation categories links
            clean: bool - places csv files into csv directory
            count: int - category list item count
        """
        self.url = url
        self.sub_url = sub_url
        self.page = page
        self.data = data
        self.about = about
        self.categories = []
        self.catlinks = []
        self.clean = clean
        self.count = 0

    def data_extract(self):
        """Extract the url page data and parses the information with BeautifulSoup
        """
        self.page = urlopen(self.url)
        self.data = self.page.read()

        self.page.close()
        soup = BeautifulSoup(self.data, "html.parser")

        return soup

    def sub_data_extract(self):
        """Extract the url page data and parses the information with BeautifulSoup
        """
        self.page = urlopen(self.sub_url)
        self.data = self.page.read()

        self.page.close()
        soup = BeautifulSoup(self.data, "html.parser")

        return soup

    def get_url(self):
        """Gets the url that the webcrawler will be accessing.
            Returns:
                url: string - the url.
            Example:
                >>> example_url = crawler.get_url()
        """
        return self.url

    def get_sub_url(self):
        """Gets the url that the webcrawler will be accessing.
            Returns:
                url: string - the url.
            Example:
                >>> example_url = crawler.get_url()
        """
        return self.sub_url

    def get_page(self):
        """Gets the page that the webcrawler is parsing data from.
            Returns:
                self.page: string - the page of the url.
            Example:
                >>> example_page = crawler.get_page()
        """
        return self.page

    def get_data(self):
        """Get the data that the webcrawler is parsing
            Returns:
                self.data: string - page data.
            Example:
                >>> example_data = crawler.get_data()
        """
        return self.data

    def get_nav_categories(self):
        """Get the categories parsed within the webcrawler.
            Returns:
                self.categories: list - list of categories within the navigation bar.
            Example:
                >>> example_categories = crawler.get_nav_categories()
        """
        return self.categories

    def get_nav_catlinks(self):
        """Get the category links within the webcrawler.
            Returns:
                self.catlinks: list - list of category links within the navigation bar.
            Example:
                >>> example_catlinks = crawler.get_nav_catlinks()
        """
        return self.catlinks

    def get_description(self):
        """Get the description of the product, located within the targeted web page.
            Returns:
                self.about: string - description of product.
            Example:
                >>> example_description = crawler.get_description()
        """
        return self.about

    def cleanup(self):
        """Clean up csv files in the current directory, and saves them to csv folder.
            Returns:
                self.clean: bool - file cleaned.
        """
        self.clean = True
        try:
            os.system(". build/move_csv.sh")
            log.info("FILE CLEAN [COMPLETED]")
        except OSError:
            print("CLEANING FAILED")
            log.warning("FILE CLEAN [FAILED]")
        return self.clean

    def open_log(self):
        """Creates log file for web-crawler.
        """
        date = datetime.now().strftime("%Y%m%d")
        time_of_day = datetime.now().strftime("%H%M%S")

        filename = "prod_extract_" + date + "_" + time_of_day + ".log"
        log.basicConfig(filename=filename, filemode='w', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



    def log_cleanup(self):
        """Clean up log files in the current directory, and saves them to log folder.
            Returns:
                self.clean: bool - file cleaned.
        """
        self.clean = True
        try:
            os.system(". build/log_clean.sh")
            log.info("FILE CLEAN [COMPLETED]")
        except OSError:
            print("CLEANING FAILED")
            log.warning("FILE CLEAN [FAILED]")
        return self.clean

    def csv_to_database(self):
        """Returns extracted csv data to an SQL database.
            Returns:
                self.clean: bool - file cleaned.
        """
        self.clean = True
        try:
            os.system("python csv_database.py")
            log.info("FILE TRANSFER [COMPLETED]")
        except OSError:
            log.warning("SQL FILE TRANSFER [FAILED]")
        return self.clean
    
    def compress(self):
        """Compresses files received from web-crawler.
        """
        self.clean = True
        try:
            os.system(". build/compress.sh")
            log.info("FILE COMPRESSION [COMPLETED]")
        except OSError:
            log.warning("FILE COMPRESSION [FAILED]")
        return self.clean
