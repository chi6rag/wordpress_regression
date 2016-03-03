from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewPostPage:
    @classmethod
    def validate_active(cls, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'post_title')))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'post_content')))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'menu_save_post')))
        except TimeoutException:
            return False

    def __init__(self, driver):
        self.driver = driver

    def enter_title(self, title):
        self.driver.find_element_by_id('post_title').send_keys(title)

    def enter_content(self, content):
        self.driver.find_element_by_id('post_content').send_keys(content)

    def click_publish(self):
        self.driver.find_element_by_id('menu_save_post').click()
