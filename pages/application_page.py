from .base_page import BasePage
from selenium.webdriver.common.by import By

class ApplicationPage(BasePage):
    VIEW_ROLE_BUTTON = (By.XPATH, "(//*[@class='btn btn-navy rounded pt-2 pr-5 pb-2 pl-5'])[1]")

    def click_view_role(self):
        self.click_element(*self.VIEW_ROLE_BUTTON)
