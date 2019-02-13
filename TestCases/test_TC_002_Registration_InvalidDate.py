from Base import InitiateDriver
from Pages import RegistrationPage


def test_invalid_date_registration():

    driver = InitiateDriver.start_browser()
    driver.close()
