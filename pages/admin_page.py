from pages.base_page import BasePage
from locator.login_page_locator import LoginPageLocator
from locator.admin_page_locator import AdminPageLocator


class AdminPage(BasePage):

    def admin_page_is_open(self):
        admin_page_header = self.find_element(AdminPageLocator.LOCATOR_ADMIN_PAGE_HEADER)
        text = 'Site administration'
        assert admin_page_header.text == text, f'admin страница не открылась'

    def login(self, email, passwd):
        login_field = self.find_element(LoginPageLocator.LOCATOR_USERNAME_INPUT)
        login_field.send_keys(email)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASW_INPUT)
        passwd_field.send_keys(passwd)
        sign_in_button = self.find_element(LoginPageLocator.LOCATOR_SUBMIT_BTN)
        sign_in_button.click()

    def create_new_user(self, username, passw):
        add_button = self.find_element(AdminPageLocator.LOCATOR_ADD_USER_BUTTON)
        add_button.click()
        username_field = self.find_element(AdminPageLocator.LOCATOR_INPUT_NEW_USER_NAME)
        username_field.send_keys(username)
        passw_field = self.find_element(AdminPageLocator.LOCATOR_INPUT_NEW_USER_PSW)
        passw_field.send_keys(passw)
        confirm_passw_field = self.find_element(AdminPageLocator.LOCATOR_INPUT_NEW_USER_PSW_CONFIRM)
        confirm_passw_field.send_keys(passw)
        continue_editing_user_button = self.find_element(AdminPageLocator.LOCATOR_NEW_USER_SAVE_CONTINUE_BUTTON)
        continue_editing_user_button.click()
        add_to_staff = self.find_element(AdminPageLocator.LOCATOR_ADD_STAFF_STATUS)
        add_to_staff.click()
        add_permissions = self.find_element(AdminPageLocator.LOCATOR_ADD_PERMISSIONS)
        add_permissions.click()
        save_user_button = self.find_element(AdminPageLocator.LOCATOR_NEW_USER_SAVE_BUTTON)
        save_user_button.click()

    def log_out(self):
        log_out_buttn = self.find_element(AdminPageLocator.LOCATOR_LOG_OUT_BUTTON)
        log_out_buttn.click()
        log_out_page_header = self.find_element(AdminPageLocator.LOCATOR_LOG_OUT_PAGE_HEADER)
        text = 'Logged out'
        assert log_out_page_header.text == text, 'log out page is not opened'
        log_in_again_button = self.find_element(AdminPageLocator.LOCATOR_LOGIN_AGAIN_BUTTON)
        log_in_again_button.click()

    def delete_post(self):
        open_post_page_button = self.find_element(AdminPageLocator.LOCATOR_OPEN_POST_PAGE)
        open_post_page_button.click()
        open_first_img = self.find_element(AdminPageLocator.LOCATOR_FIRST_POST)
        open_first_img.click()

        delete_img_button = self.find_element(AdminPageLocator.LOCATOR_DELETE_IMG_BUTTON)
        delete_img_button.click()
        confirm_delete_button = self.find_element(AdminPageLocator.LOCATOR_DELETE_IMG_SUBMIT_BUTTON)
        confirm_delete_button.click()

    def open_start_page(self):
        go_to_start_page = self.find_element(AdminPageLocator.LOCATOR_VIEW_SITE)
        go_to_start_page.click()


