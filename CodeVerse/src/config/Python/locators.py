from selenium.webdriver.common.by import By
socials={
        "instagram":[(By.CLASS_NAME,"social-icons__link"),(By.CSS_SELECTOR,'div > a[href*="instagram"]')],
        "linkedin":[(By.ID,"linkedin-in-brands"),(By.CLASS_NAME,"social-icons__link"),(By.CSS_SELECTOR,'div > a[href*="linkedin"]')]}

navbar={
        "home button":[(By.CSS_SELECTOR,'img.block-header-logo__image'),(By.CSS_SELECTOR,'header>div>a>img')],
        "how it works":[(By.CSS_SELECTOR,'a.item-content[href*="how-it-works"]')],
        "work with us":[(By.CSS_SELECTOR,'a.item-content[href*="work-with-us"]')],
        "hire codeverse":[(By.CSS_SELECTOR,'a.item-content[href*="hire-codeverse"]')],
}

hiring_you={
        "name input":[(By.CSS_SELECTOR,'form > div:nth-child(1) > input'),(By.CSS_SELECTOR,'form > div > input[placeholder="Your name"]')],
        "lname input":[(By.CSS_SELECTOR,'form > div:nth-child(2) > input'),(By.CSS_SELECTOR,'form > div > input[placeholder="Your last name"]')],
        "linkedin url input":[(By.CSS_SELECTOR,'form > div:nth-child(3) > input'),(By.CSS_SELECTOR,'form > div > input[placeholder="Linkedin URL"]')],
        "email input":[(By.CSS_SELECTOR,'form > div:nth-child(4) > input'),(By.CSS_SELECTOR,'form > div > input[placeholder="Your email address"]')],
        "message input":[(By.CSS_SELECTOR,'form > div:nth-child(5) > textarea'),(By.CSS_SELECTOR,'form > div > textarea[placeholder="Enter your message"]')],
        "submit button":[(By.CSS_SELECTOR,'button.grid-button.form__button.grid-button--primary'),By.CSS_SELECTOR,'form>button[type="submit"][name="submit"]"'],
        "thank you message":[(By.CSS_SELECTOR,'div.success-message__heading'),(By.XPATH,'//div[contains(.,"Thank You!")]')]
}

hiring_us={
        "name input":[(By.CSS_SELECTOR,'form > div:nth-child(1) > input'),(By.CSS_SELECTOR,'form > div > input[placeholder="Your name"]')],
        "lname input":[(By.CSS_SELECTOR,'form > div:nth-child(2) > input'),(By.CSS_SELECTOR,'form > div > input[placeholder="Your last name"]')],
        "email input":[(By.CSS_SELECTOR,'form > div:nth-child(3) > input'),(By.CSS_SELECTOR,'form > div > input[placeholder="Your email address"]')],
        "message input":[(By.CSS_SELECTOR,'form > div:nth-child(4) > textarea'),(By.CSS_SELECTOR,'form > div > textarea[placeholder="Enter your message"]')],
        "submit button":[(By.CSS_SELECTOR,'button.grid-button.form__button.grid-button--primary'),By.CSS_SELECTOR,'form>button[type="submit"][name="submit"]"'],
        "thank you message":[(By.CSS_SELECTOR,'div.success-message__heading'),(By.XPATH,'//div[contains(.,"Thank You!")]')]
}