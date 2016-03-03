from behave import when, step

from features import NewPostPage
from utils import DeviceUtility


@when('I enter Title as "{title}" and Message as "{message}"')
def step_impl(context, title, message):
    driver = context.driver
    new_post_page = NewPostPage(driver)
    device_utility = DeviceUtility(driver)

    new_post_page.enter_title(title)
    new_post_page.enter_content(message)
    device_utility.press_back_button()


@step('I press Publish')
def step_impl(context):
    new_post_page = NewPostPage(context.driver)
    new_post_page.click_publish()
