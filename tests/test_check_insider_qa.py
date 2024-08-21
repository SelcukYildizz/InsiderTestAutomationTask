from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.quality_assurance_page import QualityAssurancePage
from pages.application_page import ApplicationPage
from selenium.webdriver.common.by import By

class TestCheckInsiderQA(BaseTest):

    def test_check_insider_qa(self):
        home_page = HomePage(self.driver)
        careers_page = CareersPage(self.driver)
        qa_page = QualityAssurancePage(self.driver)
        app_page = ApplicationPage(self.driver)

        # Verify the main page
        self.assertEqual(self.base_url_insider, home_page.get_current_url(), "useinsider mainpage not opened")

        # Accept cookies
        home_page.click_element(By.ID, "wt-cli-accept-all-btn")

        # Navigate to Careers page
        home_page.go_to_careers_page()

        # Verify Careers page elements
        careers_page.verify_blocks_are_visible()

        # Navigate to Quality Assurance page
        careers_page.go_to_quality_assurance_page()

        # Verify QA page
        self.assertEqual("https://useinsider.com/careers/quality-assurance/", qa_page.get_current_url(), "QA page not opened")

        # Filter jobs by location and verify
        qa_page.filter_jobs_by_location()
        qa_page.verify_jobs_are_in_istanbul()
        qa_page.verify_jobs_are_in_quality_assurance()

        # Click on the View Role button and verify new tab
        qa_page.click_element(*qa_page.POSITION_1_LOCATION)
        app_page.click_view_role()

        # Switch to new tab and verify Lever application
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        self.assertIn("lever", self.driver.current_url, "Lever Application form not opened.")
