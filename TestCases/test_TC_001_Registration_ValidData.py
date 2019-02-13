from Base import InitiateDriver
from Pages import RegistrationPage
import pytest
import openpyxl
from DataGenerate import DataGen


@pytest.mark.parametrize('data', DataGen.data_generator())
def test_validate_registration(data):

    driver = InitiateDriver.start_browser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    register.enter_email('abcd@acbcd.com')
    driver.close()
