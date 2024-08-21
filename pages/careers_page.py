from .base_page import BasePage
from selenium.webdriver.common.by import By

class CareersPage(BasePage):
    LOCATIONS_TEXT = (By.CSS_SELECTOR, ".category-title-media.ml-0")
    LIFE_AT_INSIDER_TEXT = (By.XPATH, "(//h2[@class='elementor-heading-title elementor-size-default'])[2]")
    FIND_YOUR_CALLING_TEXT = (By.XPATH, "(//h3[@class='category-title-media'])[1]")
    SEE_ALL_TEAMS_BUTTON = (By.LINK_TEXT, "See all teams")
    QUALITY_ASSURANCE_BUTTON = (By.XPATH, "//img[@src='https://useinsider.com/assets/media/2021/03/qa.png']")
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//*[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']")

    def verify_blocks_are_visible(self):
        assert self.find(*self.LOCATIONS_TEXT).is_displayed(), "Locations block is not visible"
        assert self.find(*self.LIFE_AT_INSIDER_TEXT).is_displayed(), "Life at Insider block is not visible"
        assert self.find(*self.FIND_YOUR_CALLING_TEXT).is_displayed(), "Find Your Calling block is not visible"

    def go_to_quality_assurance_page(self):
        self.scroll_into_view(*self.SEE_ALL_TEAMS_BUTTON)
        self.click_with_js(*self.SEE_ALL_TEAMS_BUTTON)
        self.scroll_into_view(*self.QUALITY_ASSURANCE_BUTTON)
        self.click_with_js(*self.QUALITY_ASSURANCE_BUTTON)
