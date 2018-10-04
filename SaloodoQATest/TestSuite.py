# This python file a Test suite consists of test cases
# unittest library in python has be used to mark functions as Test cases
# Each function with unittest.TestCase as argument will be considered as a Test case
# Data, actions are loaded from TestData, ObjectRepository and PageActions files.
# Execution screenshots are saved in Screenshots folder with related test case number as file name


__author__ = "Raj"

from selenium import webdriver
import unittest
from PageActions import LoginPage
from TestData import TestSuiteData
from Objectrepository import LoginPageObjects


class LoginTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.saloodo.com/login")
        self.driver.get_screenshot_as_file('Screenshots/Setup_Login_Screen.png')        # Capture/Take Screen shot

    def test_01_verify_Login_Screen_UI_Elements(self):

        login = LoginPage(self.driver)
        login_po = LoginPageObjects(self.driver)

        self.driver.get_screenshot_as_file('Screenshots/Test_01_Login_Screen.png')      # Capture/Take Screen shot

        actual_header_text = login.get_login_header_text()                              # Step 1 : Verify Login Header
        expected_header_text = TestSuiteData.LoginHeaderText
        self.assertEqual(actual_header_text, expected_header_text)
        self.assertTrue(self.driver.find_element_by_xpath(login_po.Login_Header_Text_xpath).is_displayed())

        actual_check_box_text = login.get_login_check_box_text()                        # Step 2 : Verify checkbox
        expected_check_box_text = TestSuiteData.LoginCheckBoxText
        self.assertEqual(actual_check_box_text, expected_check_box_text)
        self.assertTrue(self.driver.find_element_by_xpath(login_po.Login_Check_Box_Text_xpath).is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath(login_po.Login_Check_Box_Text_xpath).is_enabled())

        actual_reset_pwd_text = login.get_reset_password_link_text()                    # Step 3 : Verify reset password
        expected_reset_pwd_text = TestSuiteData.LoginResetButtonText
        self.assertEqual(actual_reset_pwd_text, expected_reset_pwd_text)
        self.assertTrue(self.driver.find_element_by_xpath(login_po.Login_Reset_Password_Link_xpath).is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath(login_po.Login_Reset_Password_Link_xpath).is_enabled())

        actual_login_button_text = login.get_login_button_text()                        # Step 4 : Verify login button
        expected_login_button_text = TestSuiteData.LoginButtonText
        self.assertEqual(actual_login_button_text, expected_login_button_text)
        self.assertTrue(self.driver.find_element_by_xpath(login_po.Login_button_xpath).is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath(login_po.Login_button_xpath).is_enabled())

    def test_02_Login_with_valid_credentials(self):
        login = LoginPage(self.driver)

        login.enter_user_name(TestSuiteData.test_02_User_Name)                          # Step 1 : Enter User Name
        login.enter_password(TestSuiteData.test_02_Password)                            # Step 2 : Enter Password
        self.driver.get_screenshot_as_file('Screenshots/Test_02_Details_entered.png')   # Capture/Take Screen shot
        login.click_login()                                                             # Step 3 : Click on Login button
        self.assertEqual(self.driver.current_url, TestSuiteData.DashboardURL)           # Step 4 : Verify Login
        self.driver.get_screenshot_as_file('Screenshots/Test_02_Dashboard_Screen.png')  # Capture/Take Screen shot
        actual_user_id = login.get_user_id_on_home_screen()                                  # Step 5: Verify user ID
        expected_user_id = TestSuiteData.test_02_User_ID_Home_Screen
        self.assertEqual(expected_user_id, actual_user_id)
        login.click_logout()                                                             # Step 6 : Logout
        self.assertEqual(self.driver.current_url, TestSuiteData.LogOutURL)              # Step 7 : Verify Logout
        self.driver.get_screenshot_as_file('Screenshots/Test_02_Logout_Screen.png')     # Capture/Take Screen shot

    def test_03_Login_with_invalid_username(self):
        self.driver.refresh()

        if self.driver.current_url == TestSuiteData.LoginPageURL or self.driver.current_url == TestSuiteData.LogOutURL:
            login = LoginPage(self.driver)

            login.enter_user_name(TestSuiteData.test_03_User_Name)                      # Step 1 : Enter User Name
            login.enter_password(TestSuiteData.test_03_Password)                        # Step 2 : Enter Password
            self.driver.get_screenshot_as_file('Screenshots/Test_03_Details_entered.png')  # Capture/Take Screen shot
            login.click_login()                                                         # Step 3 : Click on Login button
            actual_error_message = login.verify_login_unsuccessful_message()               # Step 4 : Read Error Message
            expected_error_message = TestSuiteData.LoginUnsuccessfulErrorMessage
            self.assertEqual(actual_error_message, expected_error_message)              # Step 5: Verify Error Message
            self.driver.get_screenshot_as_file('Screenshots/Test_03_ErrorMsg_Screen.png')  # Capture/Take Screen shot
        else:
            self.fail("Browser is not on either Login or Logout Page")

    def test_04_Login_with_invalid_password(self):
        self.driver.refresh()

        if self.driver.current_url == TestSuiteData.LoginPageURL or self.driver.current_url == TestSuiteData.LogOutURL:
            login = LoginPage(self.driver)

            login.enter_user_name(TestSuiteData.test_04_User_Name)                      # Step 1 : Enter User Name
            login.enter_password(TestSuiteData.test_04_Password)                        # Step 2 : Enter Password
            self.driver.get_screenshot_as_file('Screenshots/Test_04_Details_Entered.png')  # Capture/Take Screen shot
            login.click_login()                                                         # Step 3 : Click on Login button
            actual_error_message = login.verify_login_unsuccessful_message()            # Step 4 : Read Error Message
            expected_error_message = TestSuiteData.LoginUnsuccessfulErrorMessage
            self.assertEqual(actual_error_message, expected_error_message)              # Step 5: Verify Error Message
            self.driver.get_screenshot_as_file('Screenshots/Test_04_ErrorMsg_Screen.png')  # Capture/Take Screen shot
        else:
            self.fail("Browser is not on either Login or Logout Page")

    def test_05_Login_without_username(self):
        self.driver.refresh()

        if self.driver.current_url == TestSuiteData.LoginPageURL or self.driver.current_url == TestSuiteData.LogOutURL:
            login = LoginPage(self.driver)

            login.enter_user_name(TestSuiteData.test_05_User_Name)                      # Step 1 : Enter User Name
            login.enter_password(TestSuiteData.test_05_Password)                        # Step 2 : Enter Password
            self.driver.get_screenshot_as_file('Screenshots/Test_05_Details_Entered.png')  # Capture/Take Screen shot
            login.click_login()                                                         # Step 3 : Click on Login button
            actual_error_message = login.get_user_name_error_message()                  # Step 4 : Read Error Message
            expected_error_message = TestSuiteData.UserNameMandatoryMessageText
            self.assertEqual(actual_error_message, expected_error_message)              # Step 5: Verify Error Message
            self.driver.get_screenshot_as_file('Screenshots/Test_05_ErrorMsg_Screen.png')  # Capture/Take Screen shot
        else:
            self.fail("Browser is not on either Login or Logout Page")

    def test_06_Login_without_password(self):
        self.driver.refresh()

        if self.driver.current_url == TestSuiteData.LoginPageURL or self.driver.current_url == TestSuiteData.LogOutURL:
            login = LoginPage(self.driver)

            login.enter_user_name(TestSuiteData.test_06_User_Name)                      # Step 1 : Enter User Name
            login.enter_password(TestSuiteData.test_06_Password)                        # Step 2 : Enter Password
            self.driver.get_screenshot_as_file('Screenshots/Test_06_Details_Entered.png')  # Capture/Take Screen shot
            login.click_login()                                                         # Step 3 : Click on Login button
            actual_error_message = login.get_password_error_message()                   # Step 4 : Read Error Message
            expected_error_message = TestSuiteData.PasswordMandatoryMessageText
            self.assertEqual(actual_error_message, expected_error_message)              # Step 5: Verify Error Message
            self.driver.get_screenshot_as_file('Screenshots/Test_06_ErrorMsg_Screen.png')  # Capture/Take Screen shot
        else:
            self.fail("Browser is not on either Login or Logout Page")

    def test_07_verify_Reset_Password_UI_Elements(self):
        self.driver.refresh()

        if self.driver.current_url == TestSuiteData.LoginPageURL or self.driver.current_url == TestSuiteData.LogOutURL:

            login = LoginPage(self.driver)
            login_po = LoginPageObjects(self.driver)

            self.driver.get_screenshot_as_file('Screenshots/Test_07_Login_Screen.png')  # Capture/Take Screen shot
            login.click_on_reset_password_link()                                        # Step 1 : Click on reset pwd

            actual_header_text = login.get_reset_password_header_text()                 # Step 2 : Verify Header text
            expected_header_text = TestSuiteData.ResetPasswordHeaderText
            self.assertEqual(actual_header_text, expected_header_text)
            self.assertTrue(self.driver.find_element_by_xpath(login_po.Reset_Password_Header_xpath).is_displayed())

            actual_message_text = login.get_reset_password_message_text()               # Step 3 : Verify message text
            expected_message_text = TestSuiteData.ResetPasswordMessageText
            self.assertEqual(actual_message_text, expected_message_text)
            self.assertTrue(self.driver.find_element_by_xpath(login_po.Reset_Password_Message_xpath).is_displayed())

            actual_button_text = login.get_reset_password_send_link_text()              # Step 4 : Verify reset button
            expected_button_text = TestSuiteData.ResetButtonText
            self.assertEqual(actual_button_text, expected_button_text)
            self.assertTrue(self.driver.find_element_by_xpath(login_po.Reset_Password_Button_xpath).is_displayed())
            self.assertTrue(self.driver.find_element_by_xpath(login_po.Reset_Password_Button_xpath).is_enabled())

                                                                                        # Step 5 : Verify email textbox
            self.assertTrue(self.driver.find_element_by_xpath(login_po.Reset_Password_Email_Textbox_xpath).is_displayed())
            self.assertTrue(self.driver.find_element_by_xpath(login_po.Reset_Password_Email_Textbox_xpath).is_enabled())

            self.driver.get_screenshot_as_file('Screenshots/Test_07_ResetPWD_Screen.png')  # Capture/Take Screen shot

        else:
            self.fail("Browser is not on either Login or Logout Page")

    def test_08_Reset_Password(self):
        self.driver.refresh()

        if self.driver.current_url == TestSuiteData.LoginPageURL or self.driver.current_url == TestSuiteData.LogOutURL:
            login = LoginPage(self.driver)

            self.driver.get_screenshot_as_file('Screenshots/Test_08_Login_Screen.png')  # Capture/Take Screen shot
            login.click_on_reset_password_link()                                        # Step 1 : Click on rest link
            login.enter_email_for_reset_password()                                      # Step 2 : Enter Email ID
            self.driver.get_screenshot_as_file('Screenshots/Test_08_Details_entered.png')  # Capture/Take Screen shot
            login.click_on_reset_password_button()                                      # Step 3 : Click on reset button
            actual_header_text = login.get_reset_success_header_text()                  # Step 4 : Read header Message
            expected_header_text = TestSuiteData.ResetSuccessHeaderText
            self.assertEqual(actual_header_text, expected_header_text)                  # Step 5: Verify header Message
            actual_success_text = login.get_reset_success_message_text()                # Step 4 : Read success Message
            expected_success_text = TestSuiteData.ResetSuccessMessageText
            self.assertEqual(actual_success_text, expected_success_text)                # Step 5: Verify success Message
            self.driver.get_screenshot_as_file('Screenshots/Test_08_Success_Screen.png')  # Capture/Take Screen shot
        else:
            self.fail("Browser is not on either Login or Logout Page")

    def test_09_login_with_keep_me_logged_in_option(self):
        self.driver.refresh()

        if self.driver.current_url == TestSuiteData.LoginPageURL or self.driver.current_url == TestSuiteData.LogOutURL:
            login = LoginPage(self.driver)

            self.driver.get_screenshot_as_file('Screenshots/Test_09_Login_Screen.png')  # Capture/Take Screen shot
            login.enter_user_name(TestSuiteData.test_09_User_Name)                      # Step 1 : Enter User Name
            login.enter_password(TestSuiteData.test_09_Password)                        # Step 2 : Enter Password
            self.driver.get_screenshot_as_file('Screenshots/Test_09_Details_Entered.png')  # Capture/Take Screen shot
            login.select_keep_me_logged_in()                                            # step 3 : select Keep me log in
            self.driver.get_screenshot_as_file('Screenshots/Test_09_keep_me_log_in.png')  # Capture/Take Screen shot
            login.click_login()                                                         # Step 4 : Click on Login button
            self.assertEqual(self.driver.current_url, TestSuiteData.DashboardURL)       # Step 5 : Verify Login
            self.driver.get_screenshot_as_file('Screenshots/Test_09_Dashboard_Screen.png')  # Capture/Take Screen shot
            actual_user_id = login.get_user_id_on_home_screen()                         # Step 6 : Verify user ID
            expected_user_id = TestSuiteData.test_09_User_ID_Home_Screen
            self.assertEqual(expected_user_id, actual_user_id)
            login.click_logout()                                                       # Step 7 : Logout
            self.assertEqual(self.driver.current_url, TestSuiteData.LogOutURL)         # Step 8 : Verify Logout
            self.driver.get_screenshot_as_file('Screenshots/Test_09_Logout_Screen.png')  # Capture/Take Screen shot
        else:
            self.fail("Browser is not on either Login or Logout Page")

    def test_10_navigate_to_login_page_from_main_page(self):
        self.driver.get("https://demo.saloodo.com")
        login = LoginPage(self.driver)                                                 # Step 1 : Navigate to main page
        self.driver.get_screenshot_as_file('Screenshots/Test_10_Main_Screen.png')      # Capture/Take Screen shot
        login.click_login_button_on_main_page()                                        # Step 2 : Click on login button
        self.assertEqual(self.driver.current_url, TestSuiteData.LoginPageURL)          # Step 3 : Verify navigated to login page
        self.driver.get_screenshot_as_file('Screenshots/Test_10_Login_Screen.png')     # Capture/Take Screen shot
