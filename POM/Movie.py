import time

from Library.selenium_code import *
from Library.data_file import *

class Pushpa(SeleniumWrapper):

    movie_objects = read_locators("Movie")

    def search_movie_name(self, value):
        search_text = Pushpa.movie_objects['search_movie']
        self.enter_text(search_text,value = value)

    def serach_movie(self,by_type, locater, text):
        self.driver.find_element(by_type, locater).send_keys(text)


    def click_movie(self):
        movie_name = Pushpa.movie_objects['movie_name']
        self.click_element(movie_name)

    def click_element(self,by_type, locater):
        self.driver.find_element(by_type,locater).click()

    def scroll_down(self, PAGE_DOWN):
        self.send_keyboard_input(PAGE_DOWN)

    def country(self):
        country_name = Pushpa.movie_objects['country_origin']
        time.sleep(2)
        self.get_text(country_name)
        time.sleep(2)

    def get_texts(self, by_type, locator):
        element = self.driver.find_element(by_type, locator)
        print(element.text)

    def release(self):
        release_date = Pushpa.movie_objects['release_date_imdb']
        self.get_text(release_date)
