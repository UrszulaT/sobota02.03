# -*- coding: utf-8 -*-

from base_page import BasePage

class HomePage(BasePage):
    def _verify_page(self):
        assert "Oficjalna strona Wizz Air" in self.driver.title

    def click_zaloguj_button(self):
        btn = self.driver.find_element()
