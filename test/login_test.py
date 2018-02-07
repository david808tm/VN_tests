from pages.home_page import HomePage
from pages.login_page import LoginPageSteps

# to define test steps WITHOUT actions, plus assert Home Page element. After all close page


class TestLogin():

    def test_login(self, login=None):
        login_steps = LoginPageSteps()
        login_steps.login("David.Kazakov@manifestmedex.org", "Password41!")

        home_page = HomePage()
        title = home_page.web_page_title()
        provider_portal = home_page.get_provider_portal_link()
        assert title
        assert provider_portal

