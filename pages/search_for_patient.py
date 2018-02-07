from pages.base_page import BasePage, BaseSteps


class SearchPanelElement(BasePage):

    def __init__(self):
        super(SearchPanelElement, self).__init__()

    def get_last_name(self):
        return self.binding.find_by_id("LastName")

    def get_first_name(self):
        return self.binding.find_by_id("FirstName")

    def get_date_of_birth(self):
        return self.binding.find_by_id("BirthDate")

    def get_search_button(self):
        return self.binding.find_by_xpath("//button[@ng-click='doSearch()']")


class SearchPanelSteps(BaseSteps):
    def __init__(self, ):
        super(SearchPanelSteps, self).__init__(SearchPanelElement())

    def search(self, last_name, first_name, date_of_birth = None, mrn = None):
        self.page.get_last_name().send_keys(last_name)
        self.page.get_first_name().send_keys(first_name)
        if date_of_birth:
            self.page.get_date_of_birth().send_keys(date_of_birth)
        self.page.get_search_button().click()

