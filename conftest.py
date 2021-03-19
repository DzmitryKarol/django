from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


username = 'testuser'
userpass = '123qwaszx'
su_name = 'admin'
su_pass = 'password'


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


#
# @pytest.fixture()
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


