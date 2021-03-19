from pages.start_page import StartPage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.database import DataBase
from conftest import username, userpass


def test_create_new_user(browser):
    start_page = StartPage(browser)
    start_page.open_base_page()
    start_page.start_page_is_open()
    start_page.open_login_page()

    login_page = LoginPage(browser)
    login_page.login_page_is_open()
    login_page.login('admin', 'password')

    admin_page = AdminPage(browser)
    admin_page.admin_page_is_open()
    admin_page.create_new_user(username, userpass)

    db = DataBase()
    db.check_user_in_db(username)

    admin_page.log_out()
    login_page.login_page_is_open()

    login_page.login(username, userpass)
    admin_page.admin_page_is_open()
    db.delete_user(username)








