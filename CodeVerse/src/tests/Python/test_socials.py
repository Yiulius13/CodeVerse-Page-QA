from src.pages.Python.HomePage import HomePage
import time

def test_one(browser,config):
    #GIVEN: CodeVerse homepage.
    
    #WHEN: User clicks "Instagram" logo.
    #THEN: Go to CodeVerse's instagram page.

    #WHEN: User clicks "Linkedin" logo.
    #THEN: Go to CodeVerse's likedin page.
    
    homepage=HomePage(browser,config)
    homepage.load()

    instagrampage=homepage.click_instagram_logo()
    url=instagrampage.return_url()
    assert url==config["instagram-url"]

    homepage.close_new_tab()

    linkedinpage=homepage.click_linkedin_logo()
    url=linkedinpage.return_url()
    assert url==config["linkedin-url"]
