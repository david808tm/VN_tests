from pages.home_page import HomePageSteps
from pages.login_page import LoginPageSteps
from pages.patient_windowlets.demo_verify import DemoSteps
from pages.patient_windowlets.problems import Problems
from pages.patient_windowlets.procedures import Procedures
from pages.provider_portal_page import ProviderPortalPage
from settings import password, login


class ComplexTest:

    def fullTest(self):
        login_steps = LoginPageSteps()
        login_steps.login(login, password)

        home_page_steps = HomePageSteps()
        home_page_steps.go_to_provider_portal()

        ProviderPortalPage.get_search_steps().search("Patient", "Martha")
        ProviderPortalPage.get_search_results().open_eye_for_patient("Patient", "Martha")

        demo_steps = DemoSteps()
        assert demo_steps.verify("Martha")


        problems = Problems()
        assert len(problems.get_all_rows()) > 0

        procedures = Procedures()
        assert len(procedures.get_all_rows()) > 0



