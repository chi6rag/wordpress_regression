from selenium.common.exceptions import NoSuchElementException


class HomePage:
    @classmethod
    def validate_active(cls, driver):
        try:
            driver.find_element_by_id('my_site_title_label')
            driver.find_element_by_id('my_site_subtitle_label')
        except NoSuchElementException, e:
            return False
