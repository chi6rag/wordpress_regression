from behave import *
from data import ValidLoginDetails
from features import HomePage, LoginPage

use_step_matcher("parse")


@given('On home page I login as a valid user and tap on New Post Icon')
def step_impl(context):
    driver = context.driver
    login_with(driver, ValidLoginDetails())
    home_page = HomePage(driver)
    home_page.tap_on_new_post_icon()


@then('I should be taken to home page')
def step_impl(context):
    HomePage.validate_active(context.driver)


def login_with(driver, valid_login_details):
    login_page = LoginPage(driver)
    login_page.enter_email(valid_login_details.username)
    login_page.enter_password(valid_login_details.password)
    login_page.login()
