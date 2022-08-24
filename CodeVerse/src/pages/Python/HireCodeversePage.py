from src.pages.Python.Page import Page
from src.config.Python import locators
class HireCodeversePage(Page):
    def __init__(self,browser):
        super().__init__(browser)
    def fill_entrys(self,name,lname,email,message):
        locator=super().return_correct_locator(self.browser,self.l_hiringus["name input"])
        name_input=self.browser.find_element(*locator)
        name_input.send_keys(name)
        
        locator=super().return_correct_locator(self.browser,self.l_hiringus["lname input"])
        lname_input=self.browser.find_element(*locator)
        lname_input.send_keys(lname)

        locator=super().return_correct_locator(self.browser,self.l_hiringus["email input"])
        email_input=self.browser.find_element(*locator)
        email_input.send_keys(email)
        
        locator=super().return_correct_locator(self.browser,self.l_hiringus["message input"])
        message_input=self.browser.find_element(*locator)
        message_input.send_keys(message)
    def click_submit_button(self):
        locator=super().return_correct_locator(self.browser,self.l_hiringus["submit button"])
        if locator==None:
            return False
        else:
            submit_button=self.browser.find_element(*locator)
            submit_button.click()
            locator=super().return_correct_locator(self.browser,self.l_hiringus["thank you message"])
            if locator==None:
                return False
            else:
                success_message=self.browser.find_element(*locator)
                return success_message.is_displayed()
    def click_home_button(self,config):
        locator=super().return_correct_locator(self.browser,self.l_navbar["home button"])
        if locator==None:
            return False
        else:
            from src.pages.Python.HomePage import HomePage
            home_button=self.browser.find_element(*locator)
            home_button.click()
            return HomePage(self.browser,config)