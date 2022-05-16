from selenium.webdriver.chrome.webdriver import WebDriver
from .web_elements import WebsiteElements as Elements


class WebsiteInterface:
    def __init__(self, browser: WebDriver):
        self.begin_button = browser.find_element(*Elements.begin_button)

    def begin(self):
        self.begin_button.click()
