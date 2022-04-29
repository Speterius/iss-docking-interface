import time
from dataclasses import dataclass
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Elements:
    """ The names of the corresponding html or css elements. """

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
    """ Parse the retreived strings into floats. (ditch the units) """

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


class WebElementInterface:
    """ This class keeps an instance of each web element so that the user can fetch data from the browser. """

    def __init__(self, browser: WebDriver):
        self.roll: WebElement = browser.find_element(*Elements.roll).find_element(*Elements.error)
        self.pitch: WebElement = browser.find_element(*Elements.pitch).find_element(*Elements.error)
        self.yaw: WebElement = browser.find_element(*Elements.yaw).find_element(*Elements.error)

        self.rollrate: WebElement = browser.find_element(*Elements.roll).find_element(*Elements.rate)
        self.pitchrate: WebElement = browser.find_element(*Elements.pitch).find_element(*Elements.rate)
        self.yawrate: WebElement = browser.find_element(*Elements.yaw).find_element(*Elements.rate)

        self.pos_x = browser.find_element(*Elements.pos_x).find_element(*Elements.pos)
        self.pos_y = browser.find_element(*Elements.pos_y).find_element(*Elements.pos)
        self.pos_z = browser.find_element(*Elements.pos_z).find_element(*Elements.pos)

        self.velocity = browser.find_element(*Elements.velocity_rate).find_element(*Elements.rate)

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

    def get_velocities(self) -> float:
        return UnitParser.parse_velocity(self.velocity.text)


def main():
    # Set up the webdriver
    service = Service("./chromedriver.exe")
    options = ChromeOptions()
    browser = Chrome(service=service, options=options)

    # options.headless = True

    # Go to the website
    browser.get("http://localhost:5555/iss-sim.spacex.com")

    # Web Element interface
    w = WebElementInterface(browser)

    print(f"waiting for 10 seconds:")
    time.sleep(15)

    # Angles
    print(w.get_angles())

    # Angular rates
    print(w.get_angular_rates())

    # Positions
    print(w.get_positions())


if __name__ == '__main__':
    main()
