class DeviceUtility:
    def __init__(self, driver):
        self.driver = driver

    def press_back_button(self):
        self.driver.press_keycode(4)