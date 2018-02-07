from pages.base_page import BasePage


class WebTable(BasePage):
    def __init__(self, xpath):
        super(WebTable, self).__init__()
        self.binding.wait_until_table_loaded(xpath)
        self.web_element = self.binding.find_by_xpath(xpath)

    def find_row_by_columns(self, column_names):
        rows = self.web_element.find_elements_by_xpath(".//div[@class = 'ui-grid-row ng-scope']")
        for row in rows:
            row_found = True
            columns = row.find_elements_by_xpath(".//div[@role = 'gridcell']")
            for column_name, value in column_names.items():
                c_index = self.find_index_by_name(column_name)
                column = columns[c_index]
                if column.text != value:
                    row_found = False
                    break
            if row_found:
                return row

    def find_index_by_name(self, name):
        header = self.web_element.find_element_by_xpath(".//div[@class = 'ui-grid-header ng-scope']")
        header_elements = header.find_elements_by_xpath(".//div[contains(@class, 'ui-grid-cell')]")
        for idx, val in enumerate(header_elements):
            if val.text == name:
                return idx


    def get_rows(self):
        rows = self.web_element.find_elements_by_xpath(".//div[@class = 'ui-grid-row ng-scope']")
        return rows