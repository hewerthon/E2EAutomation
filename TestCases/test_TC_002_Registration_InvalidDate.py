from Base import InitiateDriver
from Pages import RegistrationPage


def test_invalid_date_registration():

    driver = InitiateDriver.start_browser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_email('abcd@acbcd.com')
    driver.close()
