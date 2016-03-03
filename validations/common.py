from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def validate_presence_of_element_located_by_id \
                (id, driver, timeout):
    try:
        WebDriverWait(driver, timeout) \
            .until(EC.presence_of_element_located
                   ((By.ID, id)))
    except NoSuchElementException:
        return False
