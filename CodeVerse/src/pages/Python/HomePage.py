from src.pages.Python.Page import Page
from selenium.webdriver.common.by import By

from src.config.Python import locators





class HomePage(Page):
    def __init__(self,browser,config):
        super().__init__(browser)
        self.url=config["url"]
    def load(self):
        super().load()
        super().reload()
################################################  TEST: SOCIALS  ########################################################
    def click_instagram_logo(self):
        locator=super().return_correct_locator(self.browser,self.l_socials["instagram"])
        if locator==None:
            return False
        else:
            from src.pages.Python.InstagramPage import InstagramPage
            instagram_button=self.browser.find_element(*locator)
            instagram_button.click()
            super().switch_to_new_tab()
            return InstagramPage(self.browser)
    def click_linkedin_logo(self):
        locator=super().return_correct_locator(self.browser,self.l_socials["linkedin"])
        if locator==None:
            return False
        else:
            from src.pages.Python.LinkedinPage import LinkedinPage
            linkedin_button=self.browser.find_element(*locator)
            linkedin_button.click()
            super().switch_to_new_tab()
            return LinkedinPage(self.browser)
#######################################  TEST: HOW IT WORKS  ########################################################
    def click_how_it_works_button(self):
        locator=super().return_correct_locator(self.browser,self.l_navbar["how it works"])
        if locator==None:
            return False
        else:
            from src.pages.Python.HowItWorksPage import HowItWorksPage
            how_it_works_button=self.browser.find_element(*locator)
            how_it_works_button.click()
            return HowItWorksPage(self.browser)
#######################################  TEST: WORK WITH US  ########################################################
    def click_work_with_us_button(self):
        locator=super().return_correct_locator(self.browser,self.l_navbar["work with us"])
        if locator==None:
            return False
        else:
            from src.pages.Python.WorkWithUsPage import WorkWithUsPage
            work_with_us_button=self.browser.find_element(*locator)
            work_with_us_button.click()
            return WorkWithUsPage(self.browser)
#######################################  TEST: HIRE CODEVERSE  ########################################################
    def click_hire_codeverse_button(self):
        locator=super().return_correct_locator(self.browser,self.l_navbar["hire codeverse"])
        if locator==None:
            return False
        else:
            from src.pages.Python.HireCodeversePage import HireCodeversePage
            hire_codeverse_button=self.browser.find_element(*locator)
            hire_codeverse_button.click()
            return HireCodeversePage(self.browser)


