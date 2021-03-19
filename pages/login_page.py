from pages.base_page import BasePage
from locator.login_page_locator import LoginPageLocator


class LoginPage(BasePage):

    def login_page_is_open(self):
        login_page_header = self.find_element(LoginPageLocator.LOCATOR_LOGIN_PAGE_HEADER)
        text = 'Django administration'
        assert login_page_header.text == text, f'логин страница не открылась'

    def login(self, email, passwd):
        login_field = self.find_element(LoginPageLocator.LOCATOR_USERNAME_INPUT)
        login_field.send_keys(email)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASW_INPUT)
        passwd_field.send_keys(passwd)
        sign_in_button = self.find_element(LoginPageLocator.LOCATOR_SUBMIT_BTN)
        sign_in_button.click()
