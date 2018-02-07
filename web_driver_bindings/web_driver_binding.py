from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""why do we need WebdriverBinding? Open and close page are clear,
but why we need find_by_xpath & find_by_id
to keep all xpath and id in 1 class
return - to return elements 

after adding element to Login_test, add to Home_page AND web_driver_binding 
"""


class WebDriverBinding:

    driver = webdriver.Firefox()

    def __init__(self):
        self.webDriverWait = WebDriverWait(WebDriverBinding.driver, 5)

    def find_by_xpath(self, xpath):
        return self.webDriverWait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def find_by_clickable(self, xpath):
        return self.webDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def find_by_xpath_visibility(self, xpath):
        return self.webDriverWait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_class(self, class_attribute):
        return self.webDriverWait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_attribute)))

    def open_page(self, page):
        WebDriverBinding.driver.get(page)

    def find_by_id(self, id):
        return self.webDriverWait.until(EC.presence_of_element_located((By.ID, id)))

    def find_by_partial_link_text(self, text):
        return self.webDriverWait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, text)))

    def close_page(self):
        WebDriverBinding.driver.quit()

    def wait_until_table_loaded(self, table_locator):
        full_locator = table_locator + ".//div[@class='ui-grid-canvas']//*"
        try:
            self.webDriverWait.until(EC.presence_of_all_elements_located((By.XPATH, full_locator)))
        except TimeoutException:
            pass

