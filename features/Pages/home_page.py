from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEN_SECONDS = 10


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def validate_active(cls, driver):
        try:
            WebDriverWait(driver, TEN_SECONDS).until(EC.presence_of_element_located((By.ID, 'my_site_title_label')))
            WebDriverWait(driver, TEN_SECONDS).until(EC.presence_of_element_located((By.ID, 'my_site_subtitle_label')))
        except NoSuchElementException, exception:
            return False

    def tap_on_new_post_icon(self):
        WebDriverWait(self.driver, TEN_SECONDS).until(EC.presence_of_element_located((By.ID, 'fab_button')))
        new_post_button = self.driver.find_element_by_id('fab_button')
        new_post_button.click()
