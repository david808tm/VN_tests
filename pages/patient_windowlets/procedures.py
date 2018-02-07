from pages.table import WebTable


class Procedures():
    def get_web_table(self):
        return WebTable("//div[contains(text(), 'Procedures')]//following-sibling::div[@class='panel-body grid']")

    def get_all_rows(self):
        return self.get_web_table().get_rows()