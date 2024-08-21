from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.find(*locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_into_view(self, *locator):
        element = self.find(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_with_js(self, *locator):
        element = self.find(*locator)
        self.driver.execute_script("arguments[0].click();", element)
