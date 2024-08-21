import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from self import self
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Locators(object):
    COMPANY_BUTTON = (By.XPATH, "(//*[@class='nav-link dropdown-toggle'])[5]")
    CAREERS_BUTTON = (By.XPATH, "//a[@href='https://useinsider.com/careers/']")
    LOCATIONS_TEXT = (By.CSS_SELECTOR, ".category-title-media ml-0")
    LIFE_AT_INSIDER_TEXT = (By.XPATH, "(//h2[@class='elementor-heading-title elementor-size-default'])[2]")
    FIND_YOUR_CALLING_TEXT = (By.XPATH, "(//h3[@class='category-title-media'])[1]")
    SEE_ALL_TEAMS_BUTTON = (By.LINK_TEXT, "See all teams")
    QUALITY_ASSURANCE_BUTTON = (By.XPATH, "//img[@src='https://useinsider.com/assets/media/2021/03/qa.png']")
    SEE_ALL_QA_JOBS_BUTTON = (
        By.XPATH, "//*[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']")
    LOCATION_FILTER = (By.ID, "select2-filter-by-location-container")
    ISTANBUL_OPTION = (By.ID, "select2-filter-by-location-result-lsjv-Istanbul, Turkey")
    POSITION_1_LOCATION = (By.XPATH, "(//*[@class='position-location text-large'])[1]")
    POSITION_2_LOCATION = (By.XPATH, "(//*[@class='position-location text-large'])[2]")
    POSITION_1_DEPARTMENT = (By.XPATH, "(//*[@class='position-department text-large font-weight-600 text-primary'])[1]")
    POSITION_2_DEPARTMENT = (By.XPATH, "(//*[@class='position-department text-large font-weight-600 text-primary'])[2]")
    VIEW_ROLE_BUTTON = (By.XPATH, "(//*[@class='btn btn-navy rounded pt-2 pr-5 pb-2 pl-5'])[1]")

class TestCheckInsiderQA(unittest.TestCase):
    base_url_insider = 'https://useinsider.com/'

    def setUp(self):
        # First of all, let's set up the general browser settings, disable notifications, and configure other options.
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        # Then navigate the browser to the "useinsider" page.
        self.driver.get(self.base_url_insider)
        self.driver.implicitly_wait(10)

    def test_check_insider_qa(self):
        # First, we verify that we are on the "useinsider" page.
        self.assertEqual(self.base_url_insider, self.driver.current_url, "useinsider mainpage not opened")
        # Second we accept the cookies.
        accept_all_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
        )

        accept_all_button.click()

        # Now we click the "Company" button from the navigation bar.
        self.driver.find_element(*Locators.COMPANY_BUTTON).click()

        # Then we click the "Careers" button from the company dropdown menu.
        self.driver.find_element(*Locators.CAREERS_BUTTON).click()

        # Now we verify that if the Careers page, Locations, Teams and Life at Insider blocks are opened or not.
        expected_url = "https://useinsider.com/careers/"
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual(expected_url, current_url, "Careers page not opened")

        # I will verify Careers page from the URL and the others from the page texts if they can be seen or not.

        # Verify that the "Locations" block is visible
        LOCATIONS_TEXT = self.driver.find_element(By.CSS_SELECTOR, ".category-title-media.ml-0")
        assert LOCATIONS_TEXT.is_displayed(), "Locations block is not visible"

        # Verify that the "Life at Insider" block is visible
        LIFE_AT_INSIDER_TEXT = self.driver.find_element(*Locators.LIFE_AT_INSIDER_TEXT)
        assert LIFE_AT_INSIDER_TEXT.is_displayed(), "Life at Insider block is not visible"

        # Verify that the "Find Your Calling" block is visible
        FIND_YOUR_CALLING_TEXT = self.driver.find_element(*Locators.FIND_YOUR_CALLING_TEXT)
        assert FIND_YOUR_CALLING_TEXT.is_displayed(), "Find Your Calling block is not visible"

        # In this step I will go to "https://useinsider.com/careers/quality-assurance/" by clicking "See all teams"
        # and "Quality Assurance" buttons.

        time.sleep(5)
        see_all_teams_element = self.driver.find_element(*Locators.SEE_ALL_TEAMS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", see_all_teams_element)
        self.driver.execute_script("arguments[0].click();", see_all_teams_element)
        quality_assurance_element = self.driver.find_element(*Locators.QUALITY_ASSURANCE_BUTTON)
        # The element is in the middle of the page, so let's make the element visible first. (scroll down)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", quality_assurance_element)
        # And click the element by JavaScript Executor.
        self.driver.execute_script("arguments[0].click();", quality_assurance_element)

        # Now we are in the "https://useinsider.com/careers/quality-assurance/" page, let's verify it.

        expected_url = "https://useinsider.com/careers/quality-assurance/"
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual(expected_url, current_url, "QA page not opened")

        # In this step I will click the "See all QA jobs" according to task.

        time.sleep(5)
        see_all_qa_jobs_element = self.driver.find_element(*Locators.SEE_ALL_QA_JOBS_BUTTON)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", see_all_qa_jobs_element)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", see_all_qa_jobs_element)

        self.driver.refresh()

        # Now I will filter Location as Istanbul, Turkey
        self.driver.get("https://useinsider.com/careers/open-positions/?department=qualityassurance")
        self.driver.refresh()
        time.sleep(30)

        time.sleep(50)
        self.driver.refresh()



        filter_location_element = self.driver.find_element(*Locators.LOCATION_FILTER)
        time.sleep(30)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", filter_location_element)
        time.sleep(30)
        self.driver.execute_script("arguments[0].click();", filter_location_element)
        time.sleep(30)
        filter_location_element.click()

        self.assertIn("Istanbul, Turkey", self.driver.find_element(*Locators.POSITION_1_LOCATION).text)
        self.assertIn("Istanbul, Turkey", self.driver.find_element(*Locators.POSITION_2_LOCATION).text)

        # And then we will verify that if the results are belong to "Quality Assurance" department.

        self.assertIn("Quality Assurance", self.driver.find_element(*Locators.POSITION_1_DEPARTMENT).text)
        self.assertIn("Quality Assurance", self.driver.find_element(*Locators.POSITION_2_DEPARTMENT).text)
        time.sleep(5)

        # Now we will click the "View Role" button and the verify that if Lever Application form can be seen.
        self.driver.find_element(*Locators.POSITION_1_LOCATION).click()
        time.sleep(5)
        self.driver.find_element(*Locators.VIEW_ROLE_BUTTON).click()
        time.sleep(20)

        # As it opened in a new tab, I will get its URL and verify it.

        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        time.sleep(5)
        NEW_TAB_URL = self.driver.current_url
        time.sleep(10)
        self.assertIn("lever", NEW_TAB_URL, f"Lever Application form not opened.")

    def tearDown(self):
        # And at the last point we close the driver.
        self.driver.quit()
