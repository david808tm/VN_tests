from web_driver_bindings.web_driver_binding import WebDriverBinding


class LogoutPage:

    def __init__(self):
        self.binding = WebDriverBinding()
        self.binding.open_page("https://iehie-train.verinovum.com/#/login")

    def findUserNameField(self):
        return self.binding.find_by_id("userName")

    def findPasswordField(self):
        return self.binding.find_by_id("password")

    def findButton(self):
        return self.binding.find_by_id("submit")

    def get_bindings(self):
        return self.binding
