from selenium.webdriver.common.by import By


class AdminPageLocator:
    LOCATOR_ADMIN_PAGE_HEADER = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_ADD_USER_BUTTON = (By.XPATH, '//tr[@class="model-user"]//a[@class="addlink"]')
    LOCATOR_INPUT_NEW_USER_NAME = (By.XPATH, '//input[@id="id_username"]')
    LOCATOR_INPUT_NEW_USER_PSW = (By.XPATH, '//input[@id="id_password1"]')
    LOCATOR_INPUT_NEW_USER_PSW_CONFIRM = (By.XPATH, '//input[@id="id_password2"]')
    LOCATOR_NEW_USER_SAVE_CONTINUE_BUTTON = (By.XPATH, '//input[@name="_continue"]')
    LOCATOR_NEW_USER_SAVE_BUTTON = (By.XPATH, '//input[@name="_save"]')
    LOCATOR_ADD_STAFF_STATUS = (By.XPATH, '//input[@id="id_is_staff"]')
    LOCATOR_ADD_PERMISSIONS = (By.XPATH, '//a[@id="id_user_permissions_add_all_link"]')
    LOCATOR_LOG_OUT_BUTTON = (By.XPATH, '//div[@id="user-tools"]/a[@href="/admin/logout/"]')
    LOCATOR_LOG_OUT_PAGE_HEADER = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_LOGIN_AGAIN_BUTTON = (By.XPATH, '//div[@id="content"]//a')
    LOCATOR_OPEN_POST_PAGE = (By.XPATH, '//tr[@class="model-post"]/th/a')
    LOCATOR_FIRST_POST = (By.XPATH, '(//table[@id="result_list"]//a)[last()]')
    LOCATOR_DELETE_IMG_BUTTON = (By.XPATH, '//a[@class="deletelink"]')
    LOCATOR_DELETE_IMG_SUBMIT_BUTTON = (By.XPATH, '//input[@type="submit"]')
    LOCATOR_VIEW_SITE = (By.XPATH, '//a[text() = "View site"]')


