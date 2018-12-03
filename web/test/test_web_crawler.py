#!usr/bin/python
"""Unittest for Web Crawler.
"""
import unittest
from bs4 import BeautifulSoup
from urllib.request import urlopen
from web.src.project.web_crawler import WebCrawler

__author__ = "Disaiah Bennett"
__version__ = "0.1"

CRAWLER = WebCrawler()
CRAWLER.url = "http://www.walmart.com/"

class testFileConverts(unittest.TestCase):

    def test_data_extract_001(self):
        
        self.page = urlopen(CRAWLER.url)
        self.data = self.page.read()

        self.page.close()
        self.soup = BeautifulSoup(self.data, "html.parser")

        if self.assertEqual(self.soup, CRAWLER.data_extract()):
            return True
        else:
            return False

    def test_sub_data_extract002(self):
        self.page = urlopen(CRAWLER.url)
        self.data = self.page.read()

        self.page.close()
        self.soup = BeautifulSoup(self.data, "html.parser")

        if self.assertEqual(self.soup, CRAWLER.data_extract()):
            return True
        else:
            return False

    def test_get_url_003(self):
        self.url = CRAWLER.get_url()
        if self.assertEqual(self.url, CRAWLER.url):
            return True
        else:
            return False

    def test_get_sub_url_004(self):
        self.sub_url = CRAWLER.get_sub_url()
        if self.assertEqual(self.sub_url, CRAWLER.sub_url):
            return True
        else:
            return False

    def test_get_page_005(self):
        self.page = CRAWLER.get_page()
        if self.assertEqual(self.page, CRAWLER.page):
            return True
        else:
            return False

    def test_get_data_006(self):
        self.data = CRAWLER.get_data()
        if self.assertEqual(self.data, CRAWLER.data):
            return True
        else:
            return False

    def test_get_nav_categories_007(self):
        self.nav_categories = CRAWLER.get_nav_categories()
        if self.assertEqual(self.nav_categories, CRAWLER.categories):
            return True
        else:
            return False

    def test_get_nav_catlink_008(self):
        self.nav_catlinks = CRAWLER.get_nav_catlinks()
        if self.assertEqual(self.nav_catlinks, CRAWLER.catlinks):
            return True
        else:
            return False

    def test_get_description_009(self):
        self.about = CRAWLER.get_description()
        if self.assertEqual(self.about, CRAWLER.about):
            return True
        else:
            return False

    def test_cleanup_010(self):
        self.clean = True
        if self.assertEqual(self.clean, CRAWLER.cleanup()):
            return True
        else:
            return False

    def test_log_cleanup_011(self):
        self.log_clean = True
        if self.assertEqual(self.log_clean, CRAWLER.log_cleanup()):
            return True
        else:
            return False

    def test_csv_to_database_012(self):
        self.csv_database = True
        if self.assertEqual(self.csv_database, CRAWLER.csv_to_database()):
            return True
        else:
            return False

    def test_data_extract_failed_013(self):
        
        self.page = urlopen("http://www.google.com")
        self.data = self.page.read()

        self.page.close()
        self.soup = BeautifulSoup(self.data, "html.parser")

        if self.assertNotEqual(self.soup, CRAWLER.data_extract()):
            return True
        else:
            return False

    def test_sub_data_extract_failed_014(self):
        self.page = urlopen("http://www.google.com")
        self.data = self.page.read()

        self.page.close()
        self.soup = BeautifulSoup(self.data, "html.parser")

        if self.assertNotEqual(self.soup, CRAWLER.data_extract()):
            return True
        else:
            return False

    def test_get_url_failed_015(self):
        self.url = "http://www.google.com"
        if self.assertNotEqual(self.url, CRAWLER.url):
            return True
        else:
            return False

    def test_get_sub_url_failed_016(self):
        self.sub_url = "http://www.google.com"
        if self.assertNotEqual(self.sub_url, CRAWLER.sub_url):
            return True
        else:
            return False

    def test_get_page_failed_017(self):
        self.page = " "
        if self.assertNotEqual(self.page, CRAWLER.page):
            return True
        else:
            return False

    def test_get_data_failed_018(self):
        self.data = " "
        if self.assertNotEqual(self.data, CRAWLER.data):
            return True
        else:
            return False

    def test_get_nav_categories_failed_019(self):
        self.nav_categories = " "
        if self.assertNotEqual(self.nav_categories, CRAWLER.categories):
            return True
        else:
            return False

    def test_get_nav_catlink_failed_020(self):
        self.nav_catlinks = " "
        if self.assertNotEqual(self.nav_catlinks, CRAWLER.catlinks):
            return True
        else:
            return False

    def test_get_description_failed_021(self):
        self.about = " "
        if self.assertNotEqual(self.about, CRAWLER.about):
            return True
        else:
            return False

    def test_cleanup_failed_022(self):
        self.clean = False
        if self.assertNotEqual(self.clean, CRAWLER.cleanup()):
            return True
        else:
            return False

    def test_log_cleanup_failed_023(self):
        self.log_clean = False
        if self.assertNotEqual(self.log_clean, CRAWLER.log_cleanup()):
            return True
        else:
            return False

    def test_csv_to_database_failed_024(self):
        self.csv_database = False
        if self.assertNotEqual(self.csv_database, CRAWLER.csv_to_database()):
            return True
        else:
            return False

if __name__ == '__main__':
    unittest.main()
