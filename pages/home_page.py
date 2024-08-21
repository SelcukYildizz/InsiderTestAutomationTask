from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    COMPANY_BUTTON = (By.XPATH, "(//*[@class='nav-link dropdown-toggle'])[5]")
    CAREERS_BUTTON = (By.XPATH, "//a[@href='https://useinsider.com/careers/']")

    def go_to_careers_page(self):
        self.click_element(*self.COMPANY_BUTTON)
        self.click_element(*self.CAREERS_BUTTON)
