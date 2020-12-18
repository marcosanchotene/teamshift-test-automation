from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src import properties


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    login_button = (By.XPATH, properties.login_button_xpath)
    email_field = (By.ID, properties.login_email_field_id)
    next_button = (By.XPATH, properties.next_button_xpath)
    password_field = (By.ID, properties.password_field_id)
    second_login_button = (By.XPATH, properties.second_login_button_xpath)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.login_button).click()

    def insert_email_and_continue(self):
        email_field_element = self.driver.find_element(*LoginPage.email_field)
        email_field_element.click()
        email_field_element.send_keys(properties.email)
        self.driver.find_element(*LoginPage.next_button).click()

    def insert_password_and_continue(self):
        password_field_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LoginPage.password_field))
        password_field_element.click()
        password_field_element.send_keys(properties.password)
        self.driver.find_element(*LoginPage.second_login_button).click()


class HomePage(BasePage):

    username = (By.XPATH, properties.username_xpath)

    def check_username_loaded(self):
        username_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(HomePage.username))
        return username_element.text
