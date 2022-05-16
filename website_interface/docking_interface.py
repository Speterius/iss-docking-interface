from selenium.webdriver.chrome.webdriver import WebDriver
from contextlib import contextmanager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from .states import StateInterface
from .actions import ActionInterface
from .website_buttons import WebsiteInterface


class DockingInterface:
    def __init__(self, browser: WebDriver):
        self.states = StateInterface(browser)
        self.actions = ActionInterface(browser)
        self.website = WebsiteInterface(browser)


def iss_docking_interface(
    url: str = "http://localhost:5555/iss-sim.spacex.com",
    webdriver_path: str = "./chromedriver.exe",
) -> (WebDriver, DockingInterface):
    """This is the setup routine that returns the browser and the interface.
    The browser has to be closed at the end."""

    # Open the web browser:
    service = Service(webdriver_path)
    options = ChromeOptions()

    # Headless option might be useful later:
    # options.headless = True

    browser = Chrome(service=service, options=options)

    # Go to the website
    browser.get(url)

    # make the interface and return
    docking_inteface = DockingInterface(browser)

    return browser, docking_inteface


# Create a context manager for the interface:
@contextmanager
def iss_docking_context(
    url: str = "http://localhost:5555/iss-sim.spacex.com",
    webdriver_path: str = "./chromedriver.exe",
):
    """This is a context that can be used via the with iss_docking_context() as iss: syntax"""
    browser, docking_interface = iss_docking_interface(
        url=url, webdriver_path=webdriver_path
    )

    try:
        yield docking_interface
    finally:
        browser.close()
