from src.pages.Python.HomePage import HomePage

def test_how_it_works_button(browser,config):
    #GIVEN: Be on CodeVerse homepage.

    #WHEN: User clicks on "How it works" button.
    #THEN: Go to "How it works" section.

    homepage=HomePage(browser,config)
    homepage.load()

    howitworkspage=homepage.click_how_it_works_button()
    url=howitworkspage.return_url()
    assert url==config["howitworks-url"]
