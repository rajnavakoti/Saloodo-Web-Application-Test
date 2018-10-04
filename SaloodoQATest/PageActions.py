# This python file consists of all the page action functions of saloodo.com web application
# Each Class represents a page in the web application.
# Class consists of all the page action functions like click on login button, Enter user name, etc.,
# Test suite file will call this functions at the time of execution for necessary actions

__author__ = "Raj"

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Objectrepository import LoginPageObjects
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

    def enter_user_name(self, username):

        try:
            self.driver.find_element_by_name(LoginPageObjects.User_Name_name).clear()
            sleep(1)
            self.driver.find_element_by_name(LoginPageObjects.User_Name_name).send_keys(username)
        except NoSuchElementException:
            print("Web element you are looking for is not available on the page")

    def enter_password(self, password):

        try:
            self.driver.find_element_by_name(LoginPageObjects.Password_name).clear()
            sleep(1)
            self.driver.find_element_by_name(LoginPageObjects.Password_name).send_keys(password)
        except NoSuchElementException:
            print("Web element you are looking for is not available on the page")

    def click_login(self):

        try:
            self.driver.find_element_by_xpath(LoginPageObjects.Login_button_xpath).click()
        except NoSuchElementException:
            print("Web element you are looking for is not available on the page")

    def get_user_id_on_home_screen(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.User_ID_Home_Screen_xpath)))
        actual_user_id = self.driver.find_element_by_xpath(LoginPageObjects.User_ID_Home_Screen_xpath).text
        return actual_user_id

    def click_logout(self):

        try:
            self.driver.find_element_by_xpath(LoginPageObjects.LogOut_Button_Xpath).click()
        except NoSuchElementException:
            print("Web element you are looking for is not available on the page")

    def verify_login_unsuccessful_message(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_Error_Message_xpath)))
        actual_error_message = self.driver.find_element_by_xpath(LoginPageObjects.Login_Error_Message_xpath).text
        return actual_error_message

    def get_login_check_box_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_Check_Box_Text_xpath)))
        check_box_text = self.driver.find_element_by_xpath(LoginPageObjects.Login_Check_Box_Text_xpath).text
        return check_box_text

    def get_reset_password_link_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_Reset_Password_Link_xpath)))
        reset_password_link_text = self.driver.find_element_by_xpath(LoginPageObjects.Login_Reset_Password_Link_xpath).text
        return reset_password_link_text

    def get_login_header_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_Header_Text_xpath)))
        login_header_text = self.driver.find_element_by_xpath(LoginPageObjects.Login_Header_Text_xpath).text
        return login_header_text

    def get_login_button_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_button_xpath)))
        login_button_text = self.driver.find_element_by_xpath(LoginPageObjects.Login_button_xpath).text
        return login_button_text

    def get_user_name_error_message(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.User_Name_Mandatory_Message_xpath)))
        error_message = self.driver.find_element_by_xpath(LoginPageObjects.User_Name_Mandatory_Message_xpath).text
        return error_message

    def get_password_error_message(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Password_Mandatory_Message_xpath)))
        error_message = self.driver.find_element_by_xpath(LoginPageObjects.Password_Mandatory_Message_xpath).text
        return error_message

    def get_reset_password_header_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Reset_Password_Header_xpath)))
        header_text = self.driver.find_element_by_xpath(LoginPageObjects.Reset_Password_Header_xpath).text
        return header_text

    def get_reset_password_message_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Reset_Password_Message_xpath)))
        message_text = self.driver.find_element_by_xpath(LoginPageObjects.Reset_Password_Message_xpath).text
        return message_text

    def get_reset_password_send_link_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Reset_Password_Button_xpath)))
        message_text = self.driver.find_element_by_xpath(LoginPageObjects.Reset_Password_Button_xpath).text
        return message_text

    def click_on_reset_password_link(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_Reset_Password_Link_xpath)))
        self.driver.find_element_by_xpath(LoginPageObjects.Login_Reset_Password_Link_xpath).click()

    def enter_email_for_reset_password(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Reset_Password_Email_Textbox_xpath)))
        self.driver.find_element_by_xpath(LoginPageObjects.Reset_Password_Email_Textbox_xpath).send_keys("test+carrier@saloodo.com")

    def click_on_reset_password_button(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Reset_Password_Button_xpath)))
        self.driver.find_element_by_xpath(LoginPageObjects.Reset_Password_Button_xpath).click()

    def get_reset_success_header_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Reset_Password_Success_Header_xpath)))
        header_text = self.driver.find_element_by_xpath(LoginPageObjects.Reset_Password_Success_Header_xpath).text
        return header_text

    def get_reset_success_message_text(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Rest_Password_Success_Message_xpath)))
        message_text = self.driver.find_element_by_xpath(LoginPageObjects.Rest_Password_Success_Message_xpath).text
        return message_text

    def select_keep_me_logged_in(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_Check_Box_Text_xpath)))
        self.driver.find_element_by_xpath(LoginPageObjects.Login_Check_Box_Text_xpath).click()

    def click_login_button_on_main_page(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, LoginPageObjects.Login_button_Main_Page_xpath)))
        self.driver.find_element_by_xpath(LoginPageObjects.Login_button_Main_Page_xpath).click()

