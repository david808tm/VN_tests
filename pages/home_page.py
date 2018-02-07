from pages.base_page import BasePage, BaseSteps
from web_driver_bindings.web_driver_binding import WebDriverBinding

"""
1) import webdriver binding
2) create HomePage class, to verify that Home Page and Log out elements 
present on page. In __init__ we tie HomePage to WebDriverBinding class
3) create HomePageSteps, to click on Logout element from HomePage
class. We tie HomePageSteps to the HomePage class
"""


class HomePage(BasePage):
    def __init__(self):
        super(HomePage, self).__init__()
        self.binding = WebDriverBinding()

    def web_page_title(self):
        return self.binding.find_by_xpath("//div/h3[contains(text(), 'Home Page')]")

    def get_provider_portal_link(self):
        return self.binding.find_by_clickable("//div[@class='list-group app-list']//a[@href='/portal']")


class HomePageSteps(BaseSteps):
    def __init__(self, ):
        super(HomePageSteps, self).__init__(HomePage())

    def go_to_provider_portal(self):
        self.page.get_provider_portal_link().click()
