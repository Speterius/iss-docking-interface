import time
from dataclasses import dataclass
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Elements:
    """The names of the corresponding html or css elements."""

    roll = (By.ID, "roll")
    pitch = (By.ID, "pitch")
    yaw = (By.ID, "yaw")

    velocity_rate = (By.ID, "rate")

    pos_x = (By.ID, "x-range")
    pos_y = (By.ID, "y-range")
    pos_z = (By.ID, "z-range")

    error = (By.CSS_SELECTOR, ".error")
    rate = (By.CSS_SELECTOR, ".rate")
    pos = (By.CSS_SELECTOR, "div")


class UnitParser:
    """Parse the retreived strings into floats. (ditch the units)"""

    angle = "°"
    angular_rate = "°/s"
    position = "m"
    velocity = "m/s"

    @classmethod
    def parse_angle(cls, s: str) -> float:
        return float(s.replace(cls.angle, ""))

    @classmethod
    def parse_rate(cls, s: str) -> float:
        return float(s.replace(cls.angular_rate, ""))

    @classmethod
    def parse_position(cls, s: str) -> float:
        return float(s.replace(cls.position, ""))

    @classmethod
    def parse_velocity(cls, s: str) -> float:
        return float(s.replace(cls.velocity, ""))


def get_angle(webelement: WebElement) -> float:
    value: str = webelement.find_element(*Elements.error).text
    return UnitParser.parse_angle(value)


def get_rate(webelement: WebElement) -> float:
    value: str = webelement.find_element(*Elements.rate).text
    return UnitParser.parse_rate(value)


class StateInterface:
    """This class keeps an instance of each web element so that the user can fetch data from the browser."""

    def __init__(self, browser: WebDriver):
        self.roll: WebElement = browser.find_element(*Elements.roll).find_element(
            *Elements.error
        )
        self.pitch: WebElement = browser.find_element(*Elements.pitch).find_element(
            *Elements.error
        )
        self.yaw: WebElement = browser.find_element(*Elements.yaw).find_element(
            *Elements.error
        )

        self.rollrate: WebElement = browser.find_element(*Elements.roll).find_element(
            *Elements.rate
        )
        self.pitchrate: WebElement = browser.find_element(*Elements.pitch).find_element(
            *Elements.rate
        )
        self.yawrate: WebElement = browser.find_element(*Elements.yaw).find_element(
            *Elements.rate
        )

        self.pos_x = browser.find_element(*Elements.pos_x).find_element(*Elements.pos)
        self.pos_y = browser.find_element(*Elements.pos_y).find_element(*Elements.pos)
        self.pos_z = browser.find_element(*Elements.pos_z).find_element(*Elements.pos)

        self.velocity = browser.find_element(*Elements.velocity_rate).find_element(
            *Elements.rate
        )

    def get_angles(self) -> (float, float, float):
        roll = UnitParser.parse_angle(self.roll.text)
        pitch = UnitParser.parse_angle(self.pitch.text)
        yaw = UnitParser.parse_angle(self.yaw.text)
        return roll, pitch, yaw

    def get_angular_rates(self) -> (float, float, float):
        rollrate = UnitParser.parse_rate(self.rollrate.text)
        pitchrate = UnitParser.parse_rate(self.pitchrate.text)
        yawrate = UnitParser.parse_rate(self.yawrate.text)
        return rollrate, pitchrate, yawrate

    def get_positions(self) -> (float, float, float):
        pos_x = UnitParser.parse_position(self.pos_x.text)
        pos_y = UnitParser.parse_position(self.pos_y.text)
        pos_z = UnitParser.parse_position(self.pos_z.text)
        return pos_x, pos_y, pos_z

    def get_velocity(self) -> float:
        return UnitParser.parse_velocity(self.velocity.text)


class ActionInterface:
    def __init__(self, browser):
        self.browser = browser

        self.ctrl_pitch_up = browser.find_element(By.ID, "pitch-up-button")
        self.ctrl_pitch_down = browser.find_element(By.ID, "pitch-down-button")
        self.ctrl_roll_left = browser.find_element(By.ID, "roll-left-button")
        self.ctrl_roll_right = browser.find_element(By.ID, "roll-right-button")
        self.ctrl_yaw_left = browser.find_element(By.ID, "yaw-left-button")
        self.ctrl_yaw_right = browser.find_element(By.ID, "yaw-right-button")
        self.ctrl_translate_left = browser.find_element(By.ID, "translate-left-button")
        self.ctrl_translate_right = browser.find_element(
            By.ID, "translate-right-button"
        )
        self.ctrl_translate_up = browser.find_element(By.ID, "translate-up-button")
        self.ctrl_translate_down = browser.find_element(By.ID, "translate-down-button")
        self.ctrl_translate_forward = browser.find_element(
            By.ID, "translate-forward-button"
        )
        self.ctrl_translate_backward = browser.find_element(
            By.ID, "translate-backward-button"
        )

    def pitch_up(self):
        self.ctrl_pitch_up.click()

    def pitch_down(self):
        self.ctrl_pitch_down.click()

    def yaw_left(self):
        self.ctrl_yaw_left.click()

    def yaw_right(self):
        self.ctrl_yaw_right.click()

    def roll_left(self):
        self.ctrl_roll_left.click()

    def roll_right(self):
        self.ctrl_roll_right.click()

    def translate_left(self):
        self.ctrl_translate_left.click()

    def translate_right(self):
        self.ctrl_translate_right.click()

    def translate_up(self):
        self.ctrl_translate_up.click()

    def translate_down(self):
        self.ctrl_translate_down.click()

    def translate_forward(self):
        self.ctrl_translate_forward.click()

    def translate_backward(self):
        self.ctrl_translate_backward.click()


class DockingInterface:
    def __init__(self, browser: WebDriver):
        self.states = StateInterface(browser)
        self.actions = ActionInterface(browser)


class WebsiteInterface:
    def __init__(self, browser: WebDriver):
        self.begin_button = browser.find_element(By.ID, "begin-button")


def main():
    # Set up the webdriver
    service = Service("./chromedriver.exe")
    options = ChromeOptions()
    # options.headless = True
    with Chrome(service=service, options=options) as browser:

        # Go to the website
        browser.get("http://localhost:5555/iss-sim.spacex.com")

        # Web Element interface
        w = DockingInterface(browser)

        print(f"waiting for 15 seconds:")
        time.sleep(15)

        print(f"Pringing states for 10 seconds as a test ... ")
        for i in range(20):
            print(f"\n_____________________")
            print(f"Angles: {w.states.get_angles()}")
            print(f"Agnular rates: {w.states.get_angular_rates()}")
            print(f"Positions: {w.states.get_positions()}")
            print(f"Velocity: {w.states.get_velocity()}")

            time.sleep(1)

    print("Closing session")


if __name__ == "__main__":
    main()
