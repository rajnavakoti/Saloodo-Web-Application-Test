# This python file consists of Test data that is necessary for test execution.
# Test suite File loads test data from this file
# Below are the different test data's
# Common Test data : Used by all the test cases
# Test for test cases : Data specific for each test case

__author__ = "Raj"


class TestSuiteData:

    def __init__(self, driver):
        self.driver = driver

    # Common Test Data

    LoginPageURL = "https://demo.saloodo.com/login"
    DashboardURL = "https://demo.saloodo.com/dashboard"
    LogOutURL = "https://demo.saloodo.com/goodbye"
    LoginUnsuccessfulErrorMessage = "Either your email or password is not correct. Please ensure that you use your email address as 'Username' and try again. Alternatively, you can contact our support team at support@saloodo.com"
    LoginHeaderText = "Log in to Saloodo!"
    LoginCheckBoxText = "Keep me logged in on this computer"
    LoginResetButtonText = "Reset password"
    LoginButtonText = "LOG IN"
    UserNameMandatoryMessageText = "This field cannot be empty"
    PasswordMandatoryMessageText = "This field cannot be empty"
    ResetPasswordHeaderText = "Forgot your password?"
    ResetPasswordMessageText = "Please enter the email you used to register on Saloodo!. We will send you a link to reset your password."
    ResetPasswordErrorMessage = "This field cannot be empty"
    ResetButtonText = "SEND LINK"
    ResetSuccessHeaderText = "Please check your inbox"
    ResetSuccessMessageText = "If your email address exists in our system, we've sent you an email with instructions on how to reset your password."

    # Test Data for test cases

    # Test Case 02 : test_Login_with_valid_credentials
    test_02_User_Name = "test+carrier@saloodo.com"
    test_02_Password = "123456"
    test_02_User_ID_Home_Screen = "Test Carrier"

    # Test Case 03 : test_Login_with_invalid_username
    test_03_User_Name = "Test"
    test_03_Password = "123456"

    # Test Case 04 : test_Login_with_invalid_password
    test_04_User_Name = "test+carrier@saloodo.com"
    test_04_Password = "Raj"

    # Test Case 05 : Login_without_username
    test_05_User_Name = ""
    test_05_Password = "123456"

    # Test Case 06 : Login_without_password
    test_06_User_Name = "test+carrier@saloodo.com"
    test_06_Password = ""

    # Test Case 08 : Reset_Password
    test_08_Email = "test+carrier@saloodo.com"

    # Test Case 09 : login_with_keep_me_logged_in_option
    test_09_User_Name = "test+carrier@saloodo.com"
    test_09_Password = "123456"
    test_09_User_ID_Home_Screen = "Test Carrier"
