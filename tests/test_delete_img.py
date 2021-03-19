from pages.start_page import StartPage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from conftest import username, userpass, su_pass, su_name


def test_login(browser):
    start_page = StartPage(browser)
    start_page.open_base_page()
    start_page.start_page_is_open()
    first = start_page.get_first_post_src()
    start_page.open_login_page()
    login_page = LoginPage(browser)
    login_page.login_page_is_open()
    login_page.login(su_name, su_pass)
    admin_page = AdminPage(browser)
    admin_page.admin_page_is_open()
    admin_page.delete_post()
    admin_page.open_start_page()
    second = start_page.get_first_post_src()

    assert first != second, 'error second img equal first img'
