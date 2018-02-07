# same steps as login with elements
# pytest, Page objects, classes, methods

# 1 - create Pages.py, 2 -

from pages.home_page import HomePage
from pages.login_page import LoginPageSteps, LoginPage


# to define test steps WITHOUT actions, plus assert Home Page element. After all close page


class TestLogout():

    def test_logout(self, logout=None):

        # login_steps = LoginPageSteps()
        # login_steps.login("David.Kazakov@manifestmedex.org", "Password41!")

        home_page = HomePage()
        title = home_page.web_page_title()
        assert title

        home_page.click_on_logout_link()
        login_page = LoginPage()
        assert login_page.findButton()

