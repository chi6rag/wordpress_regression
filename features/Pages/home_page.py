from validations import *

TEN_SECONDS = 10


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def validate_active(cls, driver):
        validate_presence_of_element_located_by_id \
            ('my_site_title_label', driver, TEN_SECONDS)
        validate_presence_of_element_located_by_id \
            ('my_site_subtitle_label', driver, TEN_SECONDS)

    def tap_on_new_post_icon(self):
        fab_button_id = 'fab_button'
        validate_presence_of_element_located_by_id \
            (fab_button_id, self.driver, TEN_SECONDS)
        new_post_button = self.driver.find_element_by_id \
            (fab_button_id)
        new_post_button.click()
