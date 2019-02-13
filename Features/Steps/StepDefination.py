from behave import given, when, then
from selenium.webdriver import Chrome


@given(u'User is on registration page')
def step_impl(context):
    context.driver.get('http://thetestingworld.com/testings/')


@when(u'user enter username')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys('abcd')


@when(u'user enter email id')
def step_impl(context):
    context.driver.find_element_by_name('fld_email').send_keys('abcd@abcd.com')


@when(u'user enter password')
def step_impl(context):
    context.driver.find_element_by_name('fld_password').send_keys('abcd@1234')


@when(u'click on submit button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@value="Sign up"]').click()


@then(u'user should be logged in successfully')
def step_impl(context):
    print('Register success')


