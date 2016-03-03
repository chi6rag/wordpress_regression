from behave import when, step, then

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


@when('I enter a blank Title and Message')
def step_impl(context):
    pass


@step('I press Publish')
def step_impl(context):
    new_post_page = NewPostPage(context.driver)
    new_post_page.click_publish()


@then('I should be on new post page')
def step_impl(context):
    NewPostPage.validate_active(context.driver)
