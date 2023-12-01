from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.application import Application


# Allure command
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/Tokio-Marine_home_page_UI_components.feature
# And run the following
# allure serve test_results
def browser_init(context):
    # Browser setup for chrome
    chrome_service = Service(
        executable_path="C:\Ricky\QA\QA Autometion\Repository\Tokio-Marine-HCC-automation\chromedriver.exe")
    context.driver = webdriver.Chrome(service=chrome_service)
    context.driver.maximize_window()

    context.driver.implicitly_wait(12)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

