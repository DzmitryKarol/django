from selenium.webdriver.common.by import By


class StartPageLocator:
    LOCATOR_GO_TO_ADMIN_HEADER = (By.XPATH, '//h1[@class="jumbotron-heading"]')
    LOCATOR_GO_TO_ADMIN_BUTTON = (By.XPATH, '//a[@class="btn btn-primary my-2"]')
    LOCATOR_CREDENTIALS = (By.XPATH, '//div[@class="container"]/span')
    LOCATOR_ALL_IMG_ON_MAIN_PAGE = (By.XPATH, '//div[@class="col-md-4"]')
    LOCATOR_FIRST_IMG = (By.XPATH, '(//div[@class="card mb-4 box-shadow"])[last()]/img')
