from Base import InitiateDriver
from Pages import RegistrationPage


def test_validate_registration():

    driver = InitiateDriver.start_browser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username('Hello')
    register.enter_password('abcd')
    driver.close()
