from pages.patient_search_result_table import PatientSearchResultTable
from pages.search_for_patient import SearchPanelSteps


class ProviderPortalPage:
    search_steps = SearchPanelSteps()
    search_results = PatientSearchResultTable()

    @classmethod
    def get_search_steps(cls):
        return ProviderPortalPage.search_steps

    @classmethod
    def get_search_results(cls):
        return ProviderPortalPage.search_results






