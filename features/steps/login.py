from behave import *
from ..pages import *

use_step_matcher("parse")


@given('On home page I login using "{email}" and "{password}"')
def step_impl(context, email, password):
    login_page = LoginPage(context.driver)
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.login()


@then('I should stay on login page')
def step_impl(context):
    LoginPage.validate_active(context.driver)


@then('I should be taken to home page')
def step_impl(context):
    HomePage.validate_active(context.driver)
