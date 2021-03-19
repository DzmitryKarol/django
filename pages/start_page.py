from pages.base_page import BasePage
from locator.start_page_locator import StartPageLocator


class StartPage(BasePage):

    def start_page_is_open(self):
        start_page_header = self.find_element(StartPageLocator.LOCATOR_GO_TO_ADMIN_HEADER)
        text = 'Simple Django Application'
        assert start_page_header.text == text, f'стартовая страница не открылась'

    def open_login_page(self):
        click_login_button = self.find_element(StartPageLocator.LOCATOR_GO_TO_ADMIN_BUTTON)
        click_login_button.click()

    def get_first_post_src(self):
        first_post = self.find_element(StartPageLocator.LOCATOR_FIRST_IMG).get_attribute("src")
        return first_post
