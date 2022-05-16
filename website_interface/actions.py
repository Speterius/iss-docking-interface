from .web_elements import ActionElements as Elements
from selenium.webdriver.chrome.webdriver import WebDriver


class ActionInterface:
    """Finds and interacts with the web elements of actions."""

    def __init__(self, browser: WebDriver):
        # Angle controls:
        self.ctrl_pitch_up = browser.find_element(*Elements.pitch_up)
        self.ctrl_pitch_down = browser.find_element(*Elements.pitch_down)
        self.ctrl_roll_left = browser.find_element(*Elements.roll_left)
        self.ctrl_roll_right = browser.find_element(*Elements.roll_right)
        self.ctrl_yaw_left = browser.find_element(*Elements.yaw_left)
        self.ctrl_yaw_right = browser.find_element(*Elements.yaw_right)

        # Translational controls:
        self.ctrl_translate_left = browser.find_element(*Elements.translate_left)
        self.ctrl_translate_right = browser.find_element(*Elements.translate_right)
        self.ctrl_translate_up = browser.find_element(*Elements.translate_up)
        self.ctrl_translate_down = browser.find_element(*Elements.translate_down)
        self.ctrl_translate_forward = browser.find_element(*Elements.translate_forward)
        self.ctrl_translate_backward = browser.find_element(
            *Elements.translate_backward
        )

        # Toggle action strength
        self.ctrl_toggle_rotation_strength = browser.find_element(
            *Elements.toggle_rotation_strength
        )
        self.ctrl_toggle_translation_strength = browser.find_element(
            *Elements.toggle_translation_strength
        )

    def toggle_rotation_str(self):
        self.ctrl_toggle_rotation_strength.click()

    def toggle_translation_str(self):
        self.ctrl_toggle_translation_strength.click()

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
