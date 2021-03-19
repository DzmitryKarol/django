from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import os


username = 'testuser'
userpass = '123qwaszx'
su_name = 'admin'
su_pass = 'password'


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'reports/'+ datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


#
# @pytest.fixture()
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
