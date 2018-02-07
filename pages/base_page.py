from web_driver_bindings.web_driver_binding import WebDriverBinding


class BasePage(object):
    def __init__(self):
        self.binding = WebDriverBinding()

    def get_logout_link(self):
        logout_link = self.binding.find_by_partial_link_text("Logout")
        return logout_link

    def close_page(self):
        self.binding.close_page()


class BaseSteps(object):

    def __init__(self, page):
        self.page = page

    def click_on_logout_link(self):
        self.page.get_logout_link().click()

    def close_page(self):
        self.page.close_page()