from selenium.webdriver.chrome.webdriver import WebDriver
from .web_elements import WebsiteElements as Elements


class NoButtonError(Exception):
    pass


class WebsiteInterface:
    """This interface manages the other buttons of the website
    and checks the status of the simulation."""

    def __init__(self, browser: WebDriver):
        # Start the simulation:
        self.begin_button = browser.find_element(*Elements.begin_button)

        # Reset all positions:
        self.reset_button = browser.find_element(*Elements.reset_button)

        # Fail button displayed when failed:
        self.fail_button = browser.find_element(*Elements.fail_button)

    def is_retry_available(self) -> bool:
        """True when the try-again-button is available"""
        return self.fail_button.is_displayed()

    def is_begin_available(self) -> bool:
        """True when the begin-button is available"""
        return self.begin_button.is_displayed()

    def begin(self) -> None:
        """Click either the begin-button or the try-again button."""
        if self.is_begin_available():
            self.begin_button.click()
        elif self.is_retry_available():
            self.fail_button.click()
        else:
            raise NoButtonError(
                "Cannot begin the simulation, no begin button available"
            )

    def begin_aften_fail(self):
        self.fail_button.click()

    def reset_states(self) -> None:
        self.reset_button.click()
