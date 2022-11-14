from time import sleep
from selenium.webdriver import Chrome
from Library.Config import Config
from pytest import fixture

@fixture(scope="function")
def setup():
    print("Running Setup: Opening Browser... ")
    driver = Chrome(Config.CHROME_DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    sleep(3)
    yield driver
    print("Closing Browser")
    driver.close()
