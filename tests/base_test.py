

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    base_url_insider = 'https://useinsider.com/'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.base_url_insider)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
