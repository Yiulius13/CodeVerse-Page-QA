from src.pages.Python.HomePage import HomePage

def test_work_with_us(browser,config):
    #GIVEN: Be on CodeVerse homepage.
    
    #WHEN: User clicks on "Work with us" button.
    #THEN: Go to "Work with us" section
    
    #WHEN: User fill inputs (Name, Lname, linkedin, email, message)
    #AND: Click "submit" button.
    #THEN: "Thanks you" message is displayed.

    homepage=HomePage(browser,config)
    homepage.load()

    workwithuspage=homepage.click_work_with_us_button()
    url=workwithuspage.return_url()
    assert url==config["hiringyou-url"]

    info=config["hiring you"]
    workwithuspage.fill_entrys(*info.values())
    success=workwithuspage.click_submit_button()
    assert success

