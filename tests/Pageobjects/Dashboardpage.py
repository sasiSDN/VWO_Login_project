from selenium.webdriver.common.by import By


class Dashboard:
    def __init__(self,driver):
        self.driver=driver

    # Page Locators

    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")

    def get_user_logged(self):
        return self.driver.find_element(*Dashboard.user_logged_in)

    def get_logged_text(self):
        return self.get_user_logged().text