from selenium.webdriver import Chrome


def before_all(context):
    path = 'C:\\Users\\hsouza\\Projects\\E2EAutomation\\Driver\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)


def after_all(context):
    context.driver.close()