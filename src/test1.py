import unittest
from selenium import webdriver
import properties
import pages


class TeamShiftTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(properties.login_page_url)

    # To run this test, please set the email, password and username
    # in the properties file.
    def test_login_should_be_successful(self):
        login_page = pages.LoginPage(self.driver)
        login_page.click_login_button()
        login_page.insert_email_and_continue()
        login_page.insert_password_and_continue()
        home_page = pages.HomePage(self.driver)
        self.assertEqual(home_page.check_username_loaded(), properties.username)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
