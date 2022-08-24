from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.config.Python import locators

class Page:
    def __init__(self,browser):
        self.browser=browser
        self.l_socials=locators.socials
        self.l_navbar=locators.navbar
        self.l_hiringyou=locators.hiring_you
        self.l_hiringus=locators.hiring_us
    def return_url(self):
        return self.browser.current_url
    def load(self):
        self.browser.get(self.url)
    def reload(self):
        self.browser.refresh()
    def close_new_tab(self):
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
    def switch_to_new_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])
    def return_correct_locator(self,b,locators):
        correct_locator=None
        for locator in locators:
            try:
                b.find_element(*locator)
                correct_locator=locator
                break
            except:
                pass
        return correct_locator

