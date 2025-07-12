import time

import allure
import pytest
from selenium import webdriver
from tests.Pageobjects.LoginPage import LoginPage
from tests.Pageobjects.Dashboardpage import Dashboard

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")
    return driver

@allure.epic("vwo Login test")
@allure.feature("TC01 vwo App negative test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver=setup
    login_page=LoginPage(driver)
    login_page.Login_to_vwo(usr="admin@gmail.com",pwd="admin")
    time.sleep(5)
    error_message=login_page.get_error_msg_text()
    assert error_message == "Your email, password, IP address or location did not match"


@allure.epic("vwo Login test")
@allure.feature("TC01 vwo App negative test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver=setup
    login_page=LoginPage(driver)
    login_page.Login_to_vwo(usr="py2x@thetestingacademy.com",pwd="Wingify@1234")
    time.sleep(5)
    dashboardPage = Dashboard(driver)
    # assert "Dashboard" in driver.title
    # assert "Aman" in dashboardPage.us