# -*- coding: utf-8 -*-
import unittest
import test_data
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://wizzair.com/pl-pl/main-page#/*")
        #self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
        pass
#I Rejestracja nowego użytkownika używając adresu email - dane niepoprawne (niekompletny email)

    # def test_wrong_email(self):
    #     driver=self.driver
    #     zaloguj_btn=driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
    #     zaloguj_btn.click()
    #     #time.sleep(2)
    #     rejestracja_btn=driver.find_element_by_xpath("//button[text()='Rejestracja']")
    #     rejestracja_btn.click()
    #     #time.sleep(2)
    #     name_field=driver.find_element_by_xpath("//input[@placeholder='Imię']")
    #     name_field.send_keys(test_data.valid_name)
    #     surname_field=driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
    #     surname_field.send_keys(test_data.valid_surname)
    #     if test_data.sex=='female':
    #         gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-male"]')
    #         driver.execute_script("arguments[0].click()", gender_switch)
    #     else:
    #         gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-female"]')
    #         driver.execute_script("arguments[0].click()", gender_switch)
    #     telephone_field=driver.find_element_by_xpath("//input[@placeholder='Telefon komórkowy']")
    #     telephone_field.send_keys(test_data.valid_phone)
    #     email_field=driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
    #     email_field.send_keys(test_data.wrong_email)
    #     password_field=driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
    #     password_field.send_keys(test_data.valid_password)
    #     country_field=driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
    #     country_field.click()
    #     country_to_choose=driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']/label[164]")
    #     country_to_choose.location_once_scrolled_into_view
    #     country_to_choose.click()
    #     privacy_policy=driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"]')
    #     privacy_policy.click()
    #     register_btn=driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
    #     register_btn.click()
    #     error_notice=driver.find_element_by_xpath("(//span[contains(text(), 'Nieprawidłowy adres e-mail')])[2]")
    #
    #     assert error_notice.is_displayed()
    #     self.assertEqual(error_notice.get_attribute('innerText'), u"Nieprawidłowy adres e-mail")
    #     driver.save_screenshot('koniec.png')

    def test_wrong_name(self):
        driver=self.driver
        zaloguj_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        #time.sleep(2)
        rejestracja_btn=driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_btn.click()
        #time.sleep(2)
        name_field=driver.find_element_by_xpath("//input[@placeholder='Imię']")
        name_field.send_keys(test_data.invalid_name)
        surname_field=driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        surname_field.send_keys(test_data.invalid_surname)
        if test_data.gender=='female':
            gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            driver.execute_script("arguments[0].click()", gender_switch)
        else:
            gender_switch=driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            driver.execute_script("arguments[0].click()", gender_switch)
        telephone_field=driver.find_element_by_xpath("//input[@placeholder='Telefon komórkowy']")
        telephone_field.send_keys(test_data.valid_phone)
        email_field=driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
        email_field.send_keys(test_data.valid_email)
        password_field=driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(test_data.valid_password)
        country_field=driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
        country_field.click()
        country_to_choose=driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']/label[164]")
        country_to_choose.location_once_scrolled_into_view
        country_to_choose.click()
        privacy_policy=driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"]')
        privacy_policy.click()
        register_btn=driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        register_btn.click()

        visible_error_notices=[]
        error_notices = self.driver.find_elements_by_xpath("//span[@class='rf-input__error__message']/span")
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
#assert len(visible_error_notices)==  [ilość spodziewanych komunikatów z błedem; w zależności od danych jakie uzupełni z pliku]
        assert len(visible_error_notices) == 3
        error_text = visible_error_notices[0].get_attribute("innerText")
        assert error_text == u"Nieprawidłowy znak"

        # error_notice=driver.find_element_by_xpath("(//span[contains(text(), 'Można używać tylko liter alfabetu łacińskiego.')])[2]")

        # assert error_notice.is_displayed()
        # self.assertEqual(error_notice.get_attribute('innerText'), u"Można używać tylko liter alfabetu łacińskiego.")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
