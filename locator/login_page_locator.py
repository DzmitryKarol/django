from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_LOGIN_PAGE_HEADER = (By.XPATH, '//h1[@id="site-name"]/a')
    LOCATOR_USERNAME_INPUT = (By.XPATH, '//input[@id="id_username"]')
    LOCATOR_PASW_INPUT = (By.XPATH, '//input[@id="id_password"]')
    LOCATOR_SUBMIT_BTN = (By.XPATH, '//div[@class="submit-row"]/input')
