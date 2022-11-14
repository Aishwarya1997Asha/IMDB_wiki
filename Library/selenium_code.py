from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    # @wait_()
    def enter_text(self, element, *, value):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).clear()
        self.driver.find_element(locator_type, locator_value).send_keys(str(value))

    # @wait_()
    def click_element(self, element):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).click()

    def send_keyboard_input(self, key):
        sleep(1)
        if key.upper() not in {'ARROW_DOWN', 'ARROW_UP', 'BACK_SPACE', 'TAB', 'ENTER', 'PAGE_DOWN'}:
            raise ValueError('Keys Can be ', {'ARROW_DOWN', 'ARROW_UP', 'BACK_SPACE', 'TAB', 'ENTER', 'PAGE_DOWN'})
        action = ActionChains(self.driver)
        if key.upper() == 'ARROW_DOWN':
            action.send_keys(Keys.ARROW_DOWN).perform()
        elif key.upper() == 'ARROW_UP':
            action.send_keys(Keys.ARROW_UP).perform()
        elif key.upper() == 'BACK_SPACE':
            action.send_keys(Keys.BACK_SPACE).perform()
        elif key.upper() == 'ESCAPE':
            action.send_keys(Keys.ESCAPE).perform()
        elif key.upper() == 'TAB':
            action.send_keys(Keys.TAB).perform()
        elif key.upper() == 'ENTER':
            action.send_keys(Keys.ENTER).perform()
        elif key.upper() == 'PAGE_DOWN':
            action.send_keys(Keys.PAGE_DOWN).perform()

    def scroll_to_element(self, by_type, locator):
        element = self.driver.find_element(by_type, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_upto(self):
        self.driver.execute_script("window.scrollTo(0, 6500)")

    # @wait_()
    def get_text(self, element):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        return web_element.text

