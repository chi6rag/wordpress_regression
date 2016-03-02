from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    @classmethod
    def validate_active(cls, driver):
        try:
            driver.find_element_by_id('nux_username')
        except NoSuchElementException, e:
            return False

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'nux_sign_in_button')))

    def enter_email(self, email):
        self.driver.find_element(By.ID, 'nux_username').send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, 'nux_password').send_keys(password)

    def login(self):
        self.driver.find_element(By.ID, 'nux_sign_in_button').click()
