class NewPostPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_title(self, title):
        self.driver.find_element_by_id('post_title').send_keys(title)

    def enter_content(self, content):
        self.driver.find_element_by_id('post_content').send_keys(content)

    def click_publish(self):
        self.driver.find_element_by_id('menu_save_post').click()
