from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from .web_elements import StateElements as Elements
from .unit_parser import UnitParser


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

        # Action strength status
        self.rot_str = browser.find_element(*Elements.rotation_status)
        self.trans_str = browser.find_element(*Elements.translation_status)

    def get_rotation_str(self) -> int:
        """Returns 0 for small strength and 1 for large strength."""
        s = self.rot_str.get_attribute("class")
        return UnitParser.parse_status(s)

    def get_translation_str(self) -> int:
        """Returns 0 for small strength and 1 for large strength."""
        s = self.trans_str.get_attribute("class")
        return UnitParser.parse_status(s)

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
