from pages.base_page import BasePage, BaseSteps


class Demo(BasePage):
    def __init__(self):
        super(Demo, self).__init__()

    def demo_page(self):
        return self.binding.find_by_xpath_visibility("//div[@class = 'demo-pane']//strong")


class DemoSteps(BaseSteps):
    def __init__(self, ):
        super(DemoSteps, self).__init__(Demo())

    def verify(self, patient_name):
        header_text = self.page.demo_page().text
        if patient_name in self.page.demo_page().text:
            return True


