from src.pages.Python.HomePage import HomePage

def test_home_button(browser,config):
    #GIVEN: Be on CodeVerse homepage.
    
    #WHEN: User clicks any nav-bar's button.
    #THEN: Go to its section.
 
    #WHEN: User clicks "Home" button.
    #THEN: Go to homepage.

    homepage=HomePage(browser,config)
    homepage.load()

    howitworkspage=homepage.click_how_it_works_button()
    url=howitworkspage.return_url()
    assert url==config["howitworks-url"]
    homepage=howitworkspage.click_home_button(config)
    url=homepage.return_url()
    assert url==config["url"]

    workwithuspage=homepage.click_work_with_us_button()
    url=workwithuspage.return_url()
    assert url==config["hiringyou-url"]
    homepage=workwithuspage.click_home_button(config)
    url=homepage.return_url()
    assert url==config["url"]

    hirecodeversepage=homepage.click_hire_codeverse_button()
    url=hirecodeversepage.return_url()
    assert url==config["hiringus-url"]
    homepage=hirecodeversepage.click_home_button(config)
    url=homepage.return_url()
    assert url==config["url"]