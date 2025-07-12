from  selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")
    free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")

    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")

    #Page Actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_submit(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)


    ###Page actions
    def Login_to_vwo(self,usr,pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit().click()

    def get_error_msg_text(self):
        return self.get_error_message().text

    def get_free_trail(self):
        return  self.get_free_trail().click()











