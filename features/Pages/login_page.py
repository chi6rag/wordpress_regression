from validations import *

TEN_SECONDS = 10


class LoginPage:
    @classmethod
    def validate_active(cls, driver):
        validate_presence_of_element_located_by_id \
            ('nux_username', driver, TEN_SECONDS)
        validate_presence_of_element_located_by_id \
            ('nux_password', driver, TEN_SECONDS)
        validate_presence_of_element_located_by_id \
            ('nux_sign_in_button', driver, TEN_SECONDS)

    def __init__(self, driver):
        self.driver = driver
        validate_presence_of_element_located_by_id \
            ('nux_sign_in_button', driver, TEN_SECONDS)

    def enter_email(self, email):
        self.driver.find_element(By.ID, 'nux_username').send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, 'nux_password').send_keys(password)

    def login(self):
        self.driver.find_element(By.ID, 'nux_sign_in_button').click()
