from src.pages.Python.Page import Page

class HowItWorksPage(Page):
    def __init__(self,browser):
        super().__init__(browser)
    def click_home_button(self,config):
        locator=super().return_correct_locator(self.browser,self.l_navbar["home button"])
        if locator==None:
            return False
        else:
            from src.pages.Python.HomePage import HomePage
            home_button=self.browser.find_element(*locator)
            home_button.click()
            return HomePage(self.browser,config)