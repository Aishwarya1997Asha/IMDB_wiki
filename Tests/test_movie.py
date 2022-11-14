import time

import pytest
from selenium.webdriver.common.by import By

from POM.Movie import Pushpa


def test_movie(setup):

    p = Pushpa(setup)
    p.serach_movie(By.ID, "suggestion-search","Pushpa")

    time.sleep(5)
    p.click_element(By.XPATH, "//div[text()='Pushpa: The Rise - Part 1']")
    p.scroll_to_element(By.XPATH , "//span[text()='Details']")
    time.sleep(5)
    p.get_texts(By.XPATH, "(//a[text()='Release date']/..//a[@role='button'])[2]")

