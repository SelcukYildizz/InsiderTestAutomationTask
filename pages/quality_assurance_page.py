from .base_page import BasePage
from selenium.webdriver.common.by import By

class QualityAssurancePage(BasePage):
    LOCATION_FILTER = (By.ID, "select2-filter-by-location-container")
    ISTANBUL_OPTION = (By.ID, "select2-filter-by-location-result-lsjv-Istanbul, Turkey")
    POSITION_1_LOCATION = (By.XPATH, "(//*[@class='position-location text-large'])[1]")
    POSITION_2_LOCATION = (By.XPATH, "(//*[@class='position-location text-large'])[2]")
    POSITION_1_DEPARTMENT = (By.XPATH, "(//*[@class='position-department text-large font-weight-600 text-primary'])[1]")
    POSITION_2_DEPARTMENT = (By.XPATH, "(//*[@class='position-department text-large font-weight-600 text-primary'])[2]")

    def filter_jobs_by_location(self):
        self.scroll_into_view(*self.LOCATION_FILTER)
        self.click_element(*self.LOCATION_FILTER)
        self.click_element(*self.ISTANBUL_OPTION)

    def verify_jobs_are_in_istanbul(self):
        assert "Istanbul, Turkey" in self.find(*self.POSITION_1_LOCATION).text
        assert "Istanbul, Turkey" in self.find(*self.POSITION_2_LOCATION).text

    def verify_jobs_are_in_quality_assurance(self):
        assert "Quality Assurance" in self.find(*self.POSITION_1_DEPARTMENT).text
        assert "Quality Assurance" in self.find(*self.POSITION_2_DEPARTMENT).text
