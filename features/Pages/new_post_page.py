from validations.common import *

TEN_SECONDS = 10


class NewPostPage:
    @classmethod
    def validate_active(cls, driver):
        validate_presence_of_element_located_by_id \
            ('post_content', driver, TEN_SECONDS)
        validate_presence_of_element_located_by_id \
            ('menu_save_post', driver, TEN_SECONDS)

    def __init__(self, driver):
        self.driver = driver

    def enter_title(self, title):
        self.driver.find_element_by_id('post_title') \
            .send_keys(title)

    def enter_content(self, content):
        self.driver.find_element_by_id('post_content') \
            .send_keys(content)

    def click_publish(self):
        self.driver.find_element_by_id('menu_save_post') \
            .click()
