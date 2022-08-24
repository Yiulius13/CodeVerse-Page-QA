from src.pages.Python.HomePage import HomePage

def test_hire_codeverse(browser,config):
    #GIVEN: Be on CodeVerse home page.
    #WHEN: User clicks on "Hire Codeverse" button.
    #THEN: Be on "Hire Codeverse" section.

    #WHEN: User fill inputs (name,lname,email,message)
    #AND: User clicks "Submit" button
    #THEN: "Thanks You!" message is displayed

    homepage=HomePage(browser,config)
    homepage.load()

    hirecodeversepage=homepage.click_hire_codeverse_button()
    url=hirecodeversepage.return_url()
    assert url==config["hiringus-url"]

    info=config["hiring us"]
    hirecodeversepage.fill_entrys(*info.values())
    success=hirecodeversepage.click_submit_button()
    assert success