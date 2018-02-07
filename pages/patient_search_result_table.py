from pages.base_page import BasePage
from pages.table import WebTable


class PatientSearchResultTable(BasePage):

    def get_web_table(self):
        return WebTable("//div[@role='grid']")

    def open_eye_for_patient(self, last_name, first_name, dob=None, mrn=None):
        table = self.get_web_table()
        row_search_criteria = {"Last Name": last_name, "First Name": first_name}
        if dob:
            row_search_criteria["DOB"] = dob
        if mrn:
            row_search_criteria["MRN"] = mrn

        row = table.find_row_by_columns(row_search_criteria)

        if not row:
            raise AssertionError("There is no row that match search criteria")
        row.find_element_by_xpath(".//a[@class='glyphicon glyphicon-eye-open']").click()